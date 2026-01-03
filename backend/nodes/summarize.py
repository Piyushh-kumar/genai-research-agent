from backend.state import ResearchState
from utils.llm import get_llm

llm = get_llm()

def summarize_node(state: ResearchState) -> ResearchState:
    content = "\n".join([s["content"] for s in state["sources"]])

    prompt = f"""
    Summarize the following research clearly and concisely:

    {content}
    """

    response = llm.invoke(prompt)
    state["summary"] = response.content
    return state
