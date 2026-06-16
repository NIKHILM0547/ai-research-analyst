from pathlib import Path


REPORT_FOLDER = Path(
    "reports"
)


def get_report(company):

    filename = company.replace(
        " ",
        "_"
    )

    filepath = REPORT_FOLDER / f"{filename}.md"

    if not filepath.exists():

        return None

    with open(

        filepath,

        "r",

        encoding="utf-8"

    ) as file:

        return file.read()