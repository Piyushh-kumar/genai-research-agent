from langgraph.graph import StateGraph, END
from backend.state import ResearchState
from backend.nodes.search import search_node
from backend.nodes.approve import approve_node
from backend.nodes.summarize import summarize_node

def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("search", search_node)
    graph.add_node("approve", approve_node)
    graph.add_node("summarize", summarize_node)

    graph.set_entry_point("search")
    graph.add_edge("search", "approve")

    graph.add_conditional_edges(
        "approve",
        lambda state: "summarize" if state["approved"] else END
    )

    graph.add_edge("summarize", END)

    return graph.compile()
