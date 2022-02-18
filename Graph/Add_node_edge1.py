"""
@Author: Pradeep Panchariya
@Email : panchariya11@gmail.com
"""

def add_node(node):
    global node_counts
    #check whether node is already present or not in the graph
    if node in nodes:
        print("This node is already presented.")
    else:
        
        node_counts += 1 #count the total number of nodes
        nodes.append(node)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_counts):
            temp.append(0)
        graph.append(temp)


# add undirected/directed and unweighted/weighted edge
def add_edge(v1, v2, cost=1,type='undirected'):
  """
  v1 : verties v1
  v2 : verties v2
  cost : by default 1 
  type: directed/undirected
  rtype : None
  """
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
