from tools.web_search import web_search
from backend.state import ResearchState

def search_node(state: ResearchState) -> ResearchState:
    results = web_search.invoke(state["query"])
    state["sources"] = results
    state["approved"] = False
    return state
