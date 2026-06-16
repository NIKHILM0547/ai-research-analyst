from services.comparison_service import get_report

from services.llm_service import ask_llm


def compare_companies(

    company1,

    company2

):

    print(

        "\nCompare Agent working...\n"

    )

    report1 = get_report(

        company1

    )

    report2 = get_report(

        company2

    )

    if not report1:

        return f"{company1} report not found."

    if not report2:

        return f"{company2} report not found."

    prompt = f"""

You are a Senior Business Research Analyst.

Compare these two companies.

Company 1:

{report1}

------------------

Company 2:

{report2}

Generate:

1. Similarities

2. Differences

3. Competitive advantages

4. Risks

5. Final recommendation

"""

    return ask_llm(

        prompt

    )