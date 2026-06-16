import json

from pathlib import Path


MEMORY_FILE = Path(
    "memory/company_memory.json"
)


def save_memory(company, report):

    data = {}

    if MEMORY_FILE.exists():

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            try:

                data = json.load(
                    file
                )

            except:

                data = {}

    data[company] = report

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            data,

            file,

            indent=4

        )


def get_memory(company):

    if not MEMORY_FILE.exists():

        return None

    with open(

        MEMORY_FILE,

        "r",

        encoding="utf-8"

    ) as file:

        data = json.load(

            file

        )

    return data.get(company)