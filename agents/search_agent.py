from concurrent.futures import ThreadPoolExecutor

from services.search_service import search_business


def search_task(task):

    results = search_business(task)

    findings = []

    for item in results:

        findings.append(

            {

                "task": task,

                "title": item["title"],

                "content": item["content"],

                "url": item["url"]

            }

        )

    return findings


def perform_search(plan):

    print("\nSearch Agent working...\n")

    findings = []

    with ThreadPoolExecutor(

        max_workers=6

    ) as executor:

        results = executor.map(

            search_task,

            plan

        )

        for batch in results:

            findings.extend(

                batch

            )

    return findings