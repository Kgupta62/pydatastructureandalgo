#function to add a node using adjancency matrix representation===>
def add_node(v):
    global node_count
    if v in nodes :
        print(v,"is alreay in graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present in the graph")
    else:
        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

nodes = []
graph = []
node_count = 0
print("Before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
delete_node("C")
print("After deleting a node nodes")
print(nodes)
print(graph)
print_graph()