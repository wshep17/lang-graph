import warnings

warnings.filterwarnings("ignore", module="urllib3")

import langchain_core  # noqa: F401
from langchain_core._api.deprecation import (
    LangChainDeprecationWarning,
    LangChainPendingDeprecationWarning,
)

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
warnings.filterwarnings("ignore", category=LangChainPendingDeprecationWarning)

from typing import Annotated, TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]


def mock_llm(state: State):
    return {"messages": [{"role": "ai", "content": "Hello World"}]}


# Task 2: add another node and wire START → node_a → node_b → END
graph = StateGraph(State)

graph.add_node("mock_llm", mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()

result = graph.invoke({"messages": [{"role": "user", "content": "Hello"}]})
for message in result["messages"]:
    message.pretty_print()
