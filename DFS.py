#function to add a node using adjacency list representation===>
def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v] = []

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

#using recursion
def DFS(node,visited,graph):
    if node not in graph:
        print(node,"is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)

#using iterative approach (using stack)
def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print(node,"is not present in graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

#visited = set() #using recursive approach
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B")
add_edge("B","C")
add_edge("C","D")
add_edge("D","C")

print(graph)
#DFS("A",visited,graph)
DFSiterative("A",graph)