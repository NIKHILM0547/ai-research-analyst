from pathlib import Path


REPORT_FOLDER = Path("reports")


def save_report(company, document):

    REPORT_FOLDER.mkdir(exist_ok=True)

    filename = company.replace(" ", "_")

    filepath = REPORT_FOLDER / f"{filename}.md"

    with open(

        filepath,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(document)

    return filepath