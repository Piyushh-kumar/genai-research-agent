from typing import List, TypedDict

class ResearchState(TypedDict):
    query: str
    sources: List[dict]
    approved: bool
    summary: str
