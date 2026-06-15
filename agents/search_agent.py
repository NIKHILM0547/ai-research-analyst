from services.search_service import search_business


def perform_search(plan):

    print("\nSearch Agent working...\n")

    findings = []

    for task in plan:

        try:

            results = search_business(task)

            for item in results:

                findings.append({

                    "task": task,

                    "title": item["title"],

                    "content": item["content"],

                    "url": item["url"]

                })

        except Exception as e:

            print(f"Error researching: {task}")

            print(e)

    return findings