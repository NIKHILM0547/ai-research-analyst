from agents.memory_agent import get_memory

from services.llm_service import ask_llm


def compare_companies(company1, company2):

    print("\nCompare Agent working...\n")

    report1 = get_memory(company1)

    report2 = get_memory(company2)

    if not report1:

        return f"{company1} not found in memory."

    if not report2:

        return f"{company2} not found in memory."

    prompt = f"""

Compare these two companies.

Company 1:

{report1}

Company 2:

{report2}

Generate:

1. Similarities

2. Differences

3. Which company is stronger

4. Final Recommendation

"""

    return ask_llm(prompt)