from langchain.tools import tool
from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> list:
    """Search the web for relevant information."""
    response = tavily.search(
        query=query,
        max_results=5,
        include_answer=False
    )
    return response["results"]
