from services.llm_service import ask_llm


def analyze(findings):

    print("\nAnalyst Agent working...\n")

    findings_text = ""

    for item in findings:

        findings_text += f"""

Task: {item['task']}

Title: {item['title']}

Content: {item['content']}

Source: {item['url']}

Reliability Score: {item['score']}

"""

    prompt = f"""

You are a Senior Business Research Analyst.

Your job is to analyze company research findings.

Research Findings:

{findings_text}

Generate a professional report with these sections:

1. Executive Summary

2. Strengths

3. Weaknesses

4. Opportunities

5. Threats

6. Recommendations

Rules:

- Use bullet points
- Be concise
- Be factual
- Use information from findings only
- Do not hallucinate information

"""

    report = ask_llm(prompt)

    return report