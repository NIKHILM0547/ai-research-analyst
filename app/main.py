from workflows.research_workflow import graph

from utils.timer import start_timer

from utils.timer import stop_timer


def main():

    start = start_timer()

    company = input(

        "\nWhich company do you want to analyze?\n\n"

    )

    state = {

        "company": company

    }

    result = graph.invoke(

        state

    )

    print(

        result["document"]

    )

    elapsed = stop_timer(

        start

    )

    print(

        f"\nCompleted in {elapsed} seconds."

    )


if __name__ == "__main__":

    main()