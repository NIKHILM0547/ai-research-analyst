import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent

sys.path.append(str(ROOT))

import streamlit as st

from workflows.research_workflow import graph
from agents.compare_agent import compare_companies


st.set_page_config(
    page_title="AI Research Analyst",
    page_icon="🤖",
    layout="wide"
)


# ================= HEADER =================

st.title("🤖 AI Research Analyst")

st.markdown(
"""
Research companies, generate reports and compare businesses using AI agents.
"""
)


tab1, tab2 = st.tabs(
    [
        "🔍 Analyze Company",
        "⚖️ Compare Companies"
    ]
)


# ================= ANALYZE TAB =================

with tab1:

    st.subheader("Analyze a Company")

    company = st.text_input(
        "Enter company name",
        key="analyze_company"
    )

    if st.button(
        "🚀 Analyze Company"
    ):

        if not company:

            st.warning(
                "Please enter a company name."
            )

        else:

            progress_bar = st.progress(0)

            status_box = st.empty()

            agents = [

                "🧠 Planner Agent",

                "🔎 Search Agent",

                "✅ Validator Agent",

                "🧹 Filter Agent",

                "⭐ Source Scorer Agent",

                "📊 Analyst Agent",

                "📝 Writer Agent"

            ]

            for i, agent in enumerate(agents):

                status_box.info(
                    f"{agent} working..."
                )

                progress_bar.progress(
                    (i + 1) / len(agents)
                )

                time.sleep(0.3)

            start = time.time()

            with st.spinner(
                "🤖 Generating report..."
            ):

                result = graph.invoke(
                    {
                        "company": company
                    }
                )

            total_time = round(
                time.time() - start,
                2
            )

            progress_bar.empty()

            status_box.empty()

            st.success(
                "Analysis completed"
            )

            st.subheader(
                "📊 Execution Metrics"
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Company",
                company
            )

            col2.metric(
                "Execution Time",
                f"{total_time} sec"
            )

            col3.metric(
                "Sources Used",
                len(
                    result.get(
                        "findings",
                        []
                    )
                )
            )

            st.divider()

            st.subheader(
                "📄 Research Report"
            )

            st.markdown(
                result["document"]
            )


# ================= COMPARE TAB =================

with tab2:

    st.subheader(
        "Compare Companies"
    )

    company1 = st.text_input(
        "Company 1",
        key="compare1"
    )

    company2 = st.text_input(
        "Company 2",
        key="compare2"
    )

    if st.button(
        "⚖️ Compare"
    ):

        if not company1 or not company2:

            st.warning(
                "Enter both company names."
            )

        else:

            with st.spinner(
                "🤖 Comparing companies..."
            ):

                comparison = compare_companies(
                    company1,
                    company2
                )

            st.success(
                "Comparison completed"
            )

            st.markdown(
                comparison
            )