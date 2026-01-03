from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv("genai_project.env")

def get_llm():
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=1024
    )
