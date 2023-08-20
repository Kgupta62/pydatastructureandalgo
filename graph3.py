#function to add a node using adjacency list representation===>
def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v] = []

def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
delete_node("C")
print(graph)