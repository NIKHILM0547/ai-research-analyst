from agents.planner_agent import create_research_plan

from agents.research_executor_agent import execute_research

from agents.analyst_agent import analyze

from agents.writer_agent import create_document


def main():

    company = input(
        "\nWhich company do you want to analyze?\n\n"
    )

    plan = create_research_plan(company)

    print("\n====== RESEARCH PLAN ======\n")

    for item in plan:

        print(item)

    findings = execute_research(
        company,
        plan
    )

    report = analyze(findings)

    document = create_document(report)

    print(document)


if __name__ == "__main__":

    main()
