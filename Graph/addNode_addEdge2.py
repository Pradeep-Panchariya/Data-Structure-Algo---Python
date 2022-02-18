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
        if type=='undirected' and cost is None:
            node_dic[v1].append(v2)
            node_dic[v2].append(v1)
        elif type=='undirected' and cost is not None:
            node_dic[v1].append([v2,cost])
            node_dic[v2].append([v1, cost])
        elif type=='directed' and cost is None:
            node_dic[v1].append(v2)
        elif type=='directed' and cost is not None:
            node_dic[v1].append([v2,cost])




node_dic = {}
for i in range(65,70):
    add_node(chr(i))

add_edge('A','B',type='directed',cost=34)
add_edge('A','D',type='undirected',cost=84)
add_edge("B","E")
print(node_dic)
