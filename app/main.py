from agents.planner_agent import create_research_plan

from agents.search_agent import perform_search

from agents.validator_agent import validate_findings

from agents.source_scorer_agent import score_sources

from agents.analyst_agent import analyze

from agents.writer_agent import create_document


def main():

    company = input(

        "\nWhich company do you want to analyze?\n\n"

    )

    # Planner

    plan = create_research_plan(

        company

    )

    # Search

    findings = perform_search(

        plan

    )

    # Validator

    findings = validate_findings(

        findings

    )

    # Source Scorer

    findings = score_sources(

        findings

    )

    print(

        "\n====== SOURCES ======\n"

    )

    for item in findings:

        print(

            f"{item['score']} | {item['title']}"

        )

    # Analyst

    report = analyze(

        findings

    )

    # Writer

    document = create_document(

        report

    )

    print(

        document

    )


if __name__ == "__main__":

    main()