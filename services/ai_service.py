from services.llm_service import ask_llm


def analyze_research(findings):

    findings_text = "\n".join(findings)

    prompt = f"""

You are a senior business analyst.

Analyze these findings.

Findings:

{findings_text}

Generate:

1. Executive Summary

2. Strengths

3. Weaknesses

4. Opportunities

5. Threats

Keep it concise.

"""

    return ask_llm(prompt)