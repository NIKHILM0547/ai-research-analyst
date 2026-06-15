def validate_findings(findings):

    print("\nValidator Agent working...\n")

    cleaned = []

    seen = set()

    for item in findings:

        url = item.get("url")

        if url not in seen:

            cleaned.append(item)

            seen.add(url)

    return cleaned