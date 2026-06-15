from services.search_service import search_business


def perform_research(query):

    print("\nSearch Agent researching...\n")

    results = search_business(query)

    findings = []

    for item in results:

        findings.append(

            {

                "title": item["title"],

                "content": item["content"],

                "url": item["url"]

            }

        )

    return findings