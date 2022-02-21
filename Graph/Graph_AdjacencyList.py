"""
@Author : Pradeep Panchariya
@Email : panchariya11@gmail.com
"""


def add_node(node):
    if node in node_dic:
        print(node," is already present in graph")
    else:
        node_dic[node]=[]

def add_edge(v1,v2,cost=None,type='undirected'):
    if not v1 in node_dic:
        print(v1," is not present in graph")
    elif not v2 in node_dic:
        print(v2," is not present in graph")
    else:
        if type=='undirected' and cost is None :
            if v2 not in node_dic[v1]:
                node_dic[v1].append(v2)
            if v1 not in node_dic[v2]:
                node_dic[v2].append(v1)
        elif type=='undirected' and cost is not None:
            node_dic[v1].append([v2,cost])
            node_dic[v2].append([v1, cost])
        elif type=='directed' and cost is None:
            node_dic[v1].append(v2)
        elif type=='directed' and cost is not None:
            node_dic[v1].append([v2,cost])

def delete_node(v):
    if not v in node_dic:
        print(v, " is not present in the graph.")
    else:
        del node_dic[v]
        for k in node_dic:
            lst = node_dic[k]
            if v in lst and len(v):
                lst.remove(v)
                break

#for undirected and unweighted graph
def delete_edge(v1,v2):
    if v1 not in node_dic:
        print(v1, " is not present in graph")
    elif v2 not in node_dic:
        print(v2, " is not present in graph")
    else:
         if v1 in node_dic[v2]:
             node_dic[v1].remove(v2)
             node_dic[v2].remove(v1)

def DFS(node,visited,node_dic):
    if node not in node_dic:
        print("Node is not present in the graph ",node)
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for n in node_dic[node]:
            DFS(n,visited,node_dic)

def DFSIterative(node,node_dic):
    visited = set()
    if node not in node_dic:
        print(node, " is not present in the graph")
        return
    stack = []
    stack.append(node)
    while stack :
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in node_dic[current]:
                stack.append(i)


visited=set()
node_dic = {}
for i in range(65,75):
    add_node(chr(i))

add_edge('A','B',type='undirected')
add_edge('A','D',type='undirected')
add_edge('C','E')
add_edge('F','A')
add_edge('B','A')
add_edge('C','G')
add_edge("B","E")
add_edge('H','C')
add_edge('I','G')
add_edge('J','D')
# print(node_dic)
# delete_node("B")
# delete_edge('A','D')
print(node_dic)
DFS('A',visited,node_dic)
print('----------')
DFSIterative('A',node_dic)
