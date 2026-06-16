def filter_findings(findings):

    print("\nFilter Agent working...\n")

    blocked_domains = [

        "facebook.com",

        "instagram.com",

        "twitter.com",

        "x.com",

        "youtube.com",

        "glassdoor.com"

    ]

    filtered = []

    for item in findings:

        url = item["url"].lower()

        skip = False

        for domain in blocked_domains:

            if domain in url:

                skip = True

                break

        if not skip:

            filtered.append(item)

    return filtered