from utils.llm import get_llm

llm = get_llm()
response = llm.invoke("Explain what an AI agent is in one sentence.")
print(response.content)
