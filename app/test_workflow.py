from workflows.research_workflow import graph


state = {

    "company": "Nvidia"

}

result = graph.invoke(

    state

)

print(

    result["document"]

)