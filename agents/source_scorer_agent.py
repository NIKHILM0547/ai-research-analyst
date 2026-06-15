def score_sources(findings):

    print("\nSource Scorer Agent working...\n")

    trusted_domains = [

        ".gov",

        ".edu",

        "linkedin.com",

        "reuters.com",

        "crunchbase.com",

        "forbes.com",

        "wikipedia.org"

    ]

    scored = []

    for item in findings:

        score = 1

        url = item["url"].lower()

        for domain in trusted_domains:

            if domain in url:

                score += 4

        item["score"] = score

        scored.append(item)

    return scored