from langgraph.graph import MessagesState, StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition  #tools_condition is a function 
from langchain_core.tools import tool #tool is a decorator
from langchain_core.messages import SystemMessage

def create_conversation_graph(llm, vector_store):
  @tool(response_format='content_and_artifact')
  def retrieve_tool(query: str):
    """
    Retrieve documents relevant to the query from the vector store.
    """
    retrieved_documents = vector_store.similarity_search(query, k=3)
    serialized = "\n\n".join(
      f"Source: {doc.metadata}\nContent: {doc.page_content}"
      for doc in retrieved_documents
    )
    return serialized, retrieved_documents
  
  def query_or_respond(state: MessagesState):
    llm_with_tools = llm.bind_tools([retrieve_tool])
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}
  
  tools_node = ToolNode([retrieve_tool])

  def generate(state: MessagesState):
    recent_tool_messages = []
    for message in reversed(state["messages"]):
      if message.type == "tool":
        recent_tool_messages.append(message)
      else:
        break
    
    tool_messages = recent_tool_messages[::-1]

    docs_content = "\n\n".join(doc.content for doc in tool_messages)
    sys_msg_content = (
      "You are an assistant for answering financial news queries. "
      "Use the following retrieved context to answer the question concisely. "
      "If the answer is not in the context, say so.\n\n"
      f"{docs_content}"
    )

    conversation_msgs = [
      msg for msg in state["messages"]
      if msg.type in ("human", "system") or msg.type in ("ai" and not msg.tool_calls)
    ]

    prompt = [SystemMessage(sys_msg_content)] + conversation_msgs
    response = llm.invoke(prompt)
    return {"messages": [response]}
  
  graph_builder = StateGraph(MessagesState)
  graph_builder.add_node(query_or_respond)
  graph_builder.add_node(tools_node)
  graph_builder.add_node(generate)
  graph_builder.set_entry_point("query_or_respond")
  graph_builder.add_conditional_edges("query_or_respond", tools_condition, {END: END,
  "tools": "tools"})
  graph_builder.add_edge("tools", "generate")
  graph_builder.add_edge("generate", END)
  return graph_builder.compile()


