def approve(findings):

    print("\nHuman Approval Agent\n")

    print(

        f"{len(findings)} findings found."

    )

    answer = input(

        "\nContinue analysis? (y/n): "

    )

    if answer.lower() == "y":

        return True

    return False