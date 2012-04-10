#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.

def union(a,b):
    for i in b:
        if i not in a:
            a.append(i)

def reachable(graph, node):
    reachable_nodes=[]
    tovisit =[]
    if node in graph:
        tovisit.append(node)
        while tovisit:
            current=tovisit.pop()
            if current not in reachable_nodes:
                reachable_nodes.append(current)
                union(tovisit,graph[current])
        return reachable_nodes

#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

print reachable(graph, 'a')
#>>> ['a', 'c', 'd', 'b']

print reachable(graph, 'd')
#>>> ['d', 'a', 'c', 'b']

print reachable(graph, 'e')
#>>> ['e', 'a', 'c', 'd', 'b']

