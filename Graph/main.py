from traversal import Traversal
from cyclic import Cyclic

def undirected_graph(GraphClass):
    g = GraphClass()
    g.vertices = [1, 2, 3, 4]
    g.add_node_unidirected(1, 3)
    g.add_node_unidirected(2, 3)
    g.add_node_unidirected(0, 4)
    g.add_node_unidirected(3, 4)
    g.add_node_unidirected(1, 2)
    g.add_node_unidirected(0, 1)
    g.add_node_unidirected(1, 4)

    return g

def directed_graph(GraphClass):
    g = GraphClass()
    g.vertices = [0, 1, 2, 3]
    # g.add_node_directed(3, 3)
    g.add_node_directed(2, 3)
    g.add_node_directed(0, 2)
    # g.add_node_directed(2, 0)
    g.add_node_directed(0, 1)
    # g.add_node_directed(1, 2)

    return g

## BFS and DFS
print("TRAVERSAl::")
graph = undirected_graph(Traversal)
print("BFS: ", end="")
graph.bfs(0)
print("None")
print("DFS: ", end="")
graph.dfs(0)
print("None\n")

### Cycle
print("DIRECTED CYCLE DETECTION::")
print("Using DFS: ", end="")
graph = directed_graph(Cyclic)
ans = False
for i in graph.vertices:
    if i not in graph.visited and graph.dfs(i):
        ans = True
        break
if ans: print("Graph has cycle")
else: print("Graph do not have cycle")

print("Using BFS: ", end="")
print(f"{'Graph has cycle' if graph.bfs() else 'Graph do not have cycle'}")
