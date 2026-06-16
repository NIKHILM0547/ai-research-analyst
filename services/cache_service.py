import json

from pathlib import Path


CACHE_FILE = Path(
    "cache/company_cache.json"
)


def initialize_cache():

    CACHE_FILE.parent.mkdir(
        exist_ok=True
    )

    if not CACHE_FILE.exists():

        with open(

            CACHE_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                {},

                file

            )


def load_cache():

    initialize_cache()

    with open(

        CACHE_FILE,

        "r",

        encoding="utf-8"

    ) as file:

        return json.load(

            file

        )


def save_cache(

    company,

    document

):

    data = load_cache()

    data[company] = document

    with open(

        CACHE_FILE,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            data,

            file,

            indent=4

        )


def get_cache(

    company

):

    data = load_cache()

    return data.get(

        company

    )