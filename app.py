import streamlit as st

from backend.graph import build_graph
from utils.pdf_generator import generate_pdf

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="AI Market Research Agent",
    layout="centered"
)

st.title("AI Market Research Agent")

# -------------------------------------------------
# Build agent graph (once)
# -------------------------------------------------
graph = build_graph()

# -------------------------------------------------
# Initialize session state
# -------------------------------------------------
if "state" not in st.session_state:
    st.session_state.state = None

# -------------------------------------------------
# User input
# -------------------------------------------------
query = st.text_input("Enter company or topic")

# -------------------------------------------------
# Run research (Search node)
# -------------------------------------------------
if st.button("Run Research"):
    with st.spinner("Searching the web for relevant sources..."):
        st.session_state.state = graph.invoke({
            "query": query,
            "sources": [],
            "approved": False,
            "summary": ""
        })

# -------------------------------------------------
# Show sources + approval step
# -------------------------------------------------
if st.session_state.state and not st.session_state.state["approved"]:
    st.subheader("Sources Found")

    for s in st.session_state.state["sources"]:
        st.write(f"- {s['title']}")

    if st.button("Approve Sources"):
        st.session_state.state["approved"] = True

        # 🔴 THIS IS THE CRITICAL PART
        with st.spinner("Analyzing sources and generating summary..."):
            st.session_state.state = graph.invoke(st.session_state.state)

# -------------------------------------------------
# Show final summary
# -------------------------------------------------
if st.session_state.state and st.session_state.state.get("summary"):
    st.subheader("Final Summary")
    st.write(st.session_state.state["summary"])

    # -------------------------------------------------
    # PDF generation
    # -------------------------------------------------
    if st.button("Generate PDF Report"):
        with st.spinner("Generating PDF report..."):
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
