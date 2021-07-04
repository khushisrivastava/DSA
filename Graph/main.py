from traversal import Traversal
from cyclic_directed import Cyclic as CyclicDirected
from cyclic_undirected import Cyclic as CyclicUndirected

def undirected_graph(GraphClass):
    g = GraphClass()
    g.vertices = [0, 1, 2, 3, 4]
    g.add_node_unidirected(1, 0)
    g.add_node_unidirected(1, 2)
    g.add_node_unidirected(2, 0)
    g.add_node_unidirected(0, 3)
    g.add_node_unidirected(3, 4)

    return g

def directed_graph(GraphClass):
    g = GraphClass()
    g.vertices = [0, 1, 2, 3]
    g.add_node_directed(3, 3)
    g.add_node_directed(2, 3)
    g.add_node_directed(0, 2)
    g.add_node_directed(2, 0)
    g.add_node_directed(0, 1)
    g.add_node_directed(1, 2)

    return g

## BFS and DFS
print("TRAVERSAl::")
graph = undirected_graph(Traversal)
print("BFS: ", end="")
graph.bfs(0)
print("None")
print("DFS: ", end="")
graph.dfs(0)
print("None")

### Cycle
print("\nDIRECTED CYCLE DETECTION::")
print("Using DFS: ", end="")
graph = directed_graph(CyclicDirected)
if graph.is_cyclic_dfs(): 
    print("Graph has cycle")
else: 
    print("Graph do not have cycle")

print("Using BFS: ", end="")
if graph.bfs():
    print("Graph has cycle")
else:
    print("Graph do not have cycle")


print("\nUNDIRECTED CYCLE DETECTION::")
print("Using Union Find: ", end="")
graph = undirected_graph(CyclicUndirected)
if graph.union_find(): 
    print("Graph has cycle")
else: 
    print("Graph do not have cycle")

print("Using DFS: ", end="")
if graph.is_cyclic_dfs():
    print("Graph has cycle")
else: 
    print("Graph do not have cycle")

print("Using BFS: ", end="")
if graph.is_cyclic_bfs(): 
    print("Graph has cycle")
else: 
    print("Graph do not have cycle")
