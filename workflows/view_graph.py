from workflows.research_workflow import graph


png = graph.get_graph().draw_mermaid_png()

with open(

    "workflow.png",

    "wb"

) as file:

    file.write(

        png

    )

print(

    "workflow.png created"

)