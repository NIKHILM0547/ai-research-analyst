from services.gemini_service import ask_gemini


def analyze_research(findings):

    findings_text = "\n".join(findings)

    prompt = f"""

You are a senior business analyst.

Analyze the findings below.

Findings:

{findings_text}

Create:

1. Executive Summary

2. Strengths

3. Weaknesses

4. Opportunities

5. Threats

Keep it concise.

"""

    result = ask_gemini(prompt)

    return result