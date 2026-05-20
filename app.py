# app.py

import streamlit as st
from pipeline import run_pipeline

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# Custom Styling
# -------------------------

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.stTextInput > div > div > input {
    background-color: #1E1E1E;
    color: white;
}

.report-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #1A1A1A;
    border: 1px solid #333;
    margin-bottom: 20px;
}

.step-title {
    font-size: 24px;
    font-weight: bold;
    color: #4CAF50;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.title("🤖 Multi-Agent Research System")
st.markdown("""
This AI system uses:
- 🔍 Search Agent
- 📄 Reader Agent
- ✍️ Writer Chain
- 🧠 Critic Chain

Enter any topic and generate a complete AI research report.
""")

# -------------------------
# Input
# -------------------------

topic = st.text_input(
    "Enter Research Topic",
    placeholder="Example: Future of AI Agents"
)

# -------------------------
# Run Button
# -------------------------

if st.button("🚀 Run Research Pipeline", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Running Multi-Agent Pipeline..."):

        try:
            result = run_pipeline(topic)

            # -------------------------
            # Search Results
            # -------------------------

            st.markdown('<div class="step-title">🔍 Search Results</div>', unsafe_allow_html=True)

            st.markdown(
                f'<div class="report-box">{result["search_result"]}</div>',
                unsafe_allow_html=True
            )

            # -------------------------
            # Scraped Results
            # -------------------------

            st.markdown('<div class="step-title">📄 Scraped Content</div>', unsafe_allow_html=True)

            st.markdown(
                f'<div class="report-box">{result["scraped_result"]}</div>',
                unsafe_allow_html=True
            )

            # -------------------------
            # Final Report
            # -------------------------

            st.markdown('<div class="step-title">✍️ Generated Report</div>', unsafe_allow_html=True)

            st.markdown(
                f'<div class="report-box">{result["report"]}</div>',
                unsafe_allow_html=True
            )

            # -------------------------
            # Critic Feedback
            # -------------------------

            st.markdown('<div class="step-title">🧠 Critic Feedback</div>', unsafe_allow_html=True)

            st.markdown(
                f'<div class="report-box">{result["feedback"]}</div>',
                unsafe_allow_html=True
            )

            st.success("Pipeline Completed Successfully ✅")

        except Exception as e:
            st.error(f"Error: {str(e)}")