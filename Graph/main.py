from traversal import Traversal
from cyclic_directed import Cyclic as CyclicDirected
from cyclic_undirected import Cyclic as CyclicUndirected
from dijkstra_adjancy_list import Dijktra
from dijksta_adjancy_matrix import Graph as DijkstraAdjancyMatrix
from bellman_ford import BellmanFord
from floyd_warshall import FloydWarshall
from prims_adjancy_list import Prims
from prims_adjancy_matrix import Graph as PrimsAdjancyMatrix
from kruskal import Krushkal
from topological_sort import TopologicalSort
from kahn_algorithm import Kahn

def undirected_graph(GraphClass):
    g = GraphClass()
    g.vertices = [0, 1, 2, 3, 4]
    g.add_node_undirected(1, 0)
    g.add_node_undirected(1, 2)
    g.add_node_undirected(2, 0)
    g.add_node_undirected(0, 3)
    g.add_node_undirected(3, 4)

    return g

def undirected_weighted_graph(GraphClass):
    g = GraphClass()
    g.vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    g.add_node_weighted_undirected(0, 1, 4)
    g.add_node_weighted_undirected(0, 7, 8)
    g.add_node_weighted_undirected(1, 2, 8)
    g.add_node_weighted_undirected(1, 7, 11)
    g.add_node_weighted_undirected(2, 3, 7)
    g.add_node_weighted_undirected(2, 8, 2)
    g.add_node_weighted_undirected(2, 5, 4)
    g.add_node_weighted_undirected(3, 4, 9)
    g.add_node_weighted_undirected(3, 5, 14)
    g.add_node_weighted_undirected(4, 5, 10)
    g.add_node_weighted_undirected(5, 6, 2)
    g.add_node_weighted_undirected(6, 7, 1)
    g.add_node_weighted_undirected(6, 8, 6)
    g.add_node_weighted_undirected(7, 8, 7)
    
    return g

def directed_graph(GraphClass):
    g = GraphClass()
    g.vertices = [0, 1, 2, 3, 4, 5]
    g.add_node_directed(5, 0)
    g.add_node_directed(5, 2)
    g.add_node_directed(4, 0)
    g.add_node_directed(4, 1)
    g.add_node_directed(2, 3)
    g.add_node_directed(3, 1)

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

## Dijkstra
print("\nAdjancy List Dijstra:")
graph = undirected_weighted_graph(Dijktra)
graph.dijkstra(0)

print("\nAdjancy Matrix Dijkstra:")
g = DijkstraAdjancyMatrix(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
g.dijkstra(0);

## Bellman Ford
print("\nBellmanFord:")
graph = undirected_weighted_graph(BellmanFord)
graph.bellman_ford(0)

## Floyd Warshall
print("\nFloyd Warshall:")
g = FloydWarshall(4)
g.graph = [[0, 5, -1, 10],
        [-1, 0, 3, -1],
        [-1, -1, 0,   1],
        [-1, -1, -1, 0]
    ]
g.floyd_warshall()

## Prims
print("\nAdjancy List Prims:")
graph = undirected_weighted_graph(Prims)
graph.prims(0)

print("\nAdjancy Matrix Prims")
g = PrimsAdjancyMatrix(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
g.prims(0);

## Kruskal
print("\nAdjancy List Krushkal")
g = undirected_weighted_graph(Krushkal)
g.kruskal()

## Topological Sort
print("\nTopological Sort::")
s = directed_graph(TopologicalSort)
s.topological_sort()

## Kahn's Algorithm
print("\nKahn's Algorithm")
s = directed_graph(Kahn)
s.kahn()
