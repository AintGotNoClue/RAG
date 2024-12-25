from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from utils.llm_utils import query_ollama

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def ollama_chatbot(state: State):
    user_message = state["messages"][-1]
    if isinstance(user_message, dict):
        content = user_message["content"]
    else:
        content = user_message.content
    response = query_ollama(content)
    return {"messages": state["messages"] + [{"role": "assistant", "content": response}]}


graph_builder.add_node("ollama_chatbot", ollama_chatbot)
graph_builder.add_edge(START, "ollama_chatbot")
graph_builder.add_edge("ollama_chatbot", END)

graph = graph_builder.compile()
