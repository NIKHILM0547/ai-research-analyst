def build_metrics(state):

    metrics = {

        "company": state.get(

            "company"

        ),

        "cache_used": state.get(

            "cached",

            False

        ),

        "plan_count": len(

            state.get(

                "plan",

                []

            )

        ),

        "source_count": len(

            state.get(

                "findings",

                []

            )

        )

    }

    return metrics