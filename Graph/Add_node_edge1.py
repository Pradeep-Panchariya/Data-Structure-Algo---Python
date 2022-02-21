"""
@Author: Pradeep Panchariya
@Email : panchariya11@gmail.com
"""

def add_node(node):
    global node_counts
    if node in nodes:
        print("This node is already presented.")
    else:
        node_counts += 1
        nodes.append(node)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_counts):
            temp.append(0)
        graph.append(temp)


# add undirected/directed and unweighted/weighted edge
def add_edge(v1, v2, cost=1,type='undirected'):
    if not v1 in nodes:
        print(v1, " node is not present")
    elif not v2 in nodes:
        print(v2, " node is not present")
    else:
        index_v1 = nodes.index(v1)
        index_v2 = nodes.index(v2)
        if type=='undirected':
            graph[index_v1][index_v2] = cost
            graph[index_v2][index_v1] = cost
        elif type=='directed':
            graph[index_v1][index_v2]=cost

def delete_node(v):
    global node_counts
    if not v in nodes:
        print(v," is not present in the graph")
    else:
        index_v = nodes.index(v)
        node_counts-=1
        nodes.remove((v))
        for n in graph:
            n.pop(index_v)
        graph.pop(index_v)


def delete_edge(v1,v2,type='undirected'):
    if not v1 in nodes:
        print(v1, " is not present in graph")
    elif not v2 in nodes:
        print(v2, " is not presetn in graph")
    else:
        index_v1 = nodes.index(v1)
        index_v2 = nodes.index(v2)
        if type=='undirected':
            graph[index_v1][index_v2]=0
            graph[index_v2][index_v1]=0
        elif type=='directed':
            graph[index_v1][index_v2]=0

def print_graph():
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=" ")
        print()


# Create a list for Nodes
nodes = []
graph = []
node_counts = 0

print("Before adding the Node")
print("Nodes: ", nodes)
print("Graph: ", graph)

add_node("A")
add_node("B")
add_node("C")
add_node("D")
print("After adding the Node")
print("Nodes: ", nodes)
print("Graph: ", graph)

add_edge("A", "C",78,'undirected')
print_graph()
print(graph)
delete_node("B")
print_graph()
print(graph)
delete_edge('A','C',type='undirected')
print_graph()
