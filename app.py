import streamlit as st
from backend.graph import build_graph

st.set_page_config(page_title="AI Research Agent", layout="centered")
st.title("AI Market Research Agent")

graph = build_graph()

query = st.text_input("Enter company or topic")

if "state" not in st.session_state:
    st.session_state.state = None

if st.button("Run Research"):
    st.session_state.state = graph.invoke({
        "query": query,
        "sources": [],
        "approved": False,
        "summary": ""
    })

if st.session_state.state and not st.session_state.state["approved"]:
    st.subheader("Sources Found")
    for s in st.session_state.state["sources"]:
        st.write(f"- {s['title']}")

    if st.button("Approve Sources"):
        st.session_state.state["approved"] = True
        st.session_state.state = graph.invoke(st.session_state.state)

if st.session_state.state and st.session_state.state.get("summary"):
    st.subheader("Final Summary")
    st.write(st.session_state.state["summary"])


from utils.pdf_generator import generate_pdf
import os

if st.session_state.state and st.session_state.state.get("summary"):
    if st.button("Generate PDF Report"):
        filename = "research_report.pdf"
        generate_pdf(
            query=st.session_state.state["query"],
            sources=st.session_state.state["sources"],
            summary=st.session_state.state["summary"],
            filename=filename
        )

        with open(filename, "rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name=filename,
                mime="application/pdf"
            )
