# <center>**Graphs**
<br>

## **Graph Data Structure:**
It is a collection of nodes that cointains data and are connected to other nodes.<br>
Everything that has data is a node and every relationship is an edge from one node to another.
<br>

### Terminologies:
- **Adjacency**: A vertex is adjacent to another vertex if there is a node connecting them.
- **Path**: Sequence of edges that allow to go from 1 vertex to another.
- **Directed Graph**: Edges in the graph are represented with arrows to show the direction of the edge.
- **Unidirected Graph**: Edges do not point in any direction, they are bidirectional.
- **Connected Graph**: Graph in which there is always a path between twp vertices.
<br>

### Representation:
- **Adjacency Matrix:**
    - If there is a edge connecting vertex `i` and `j`, value of element `a[i][j] = 1` in matrix.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/adjacency-matrix_1.png" >
    - Edge lookup is fast but occupies more space.

- **Adjacency List:**
    - Represented as array of linked list.
    - Each element in the list is vertex of linked list contained all the other elements it forms link(edge) with.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/adjacency-list.png" >
    - Very space effecient.
<br>

### Operations:
- Element loopup
- Add elements
- Traverse 
- Find path between vertices.

****************************************************************************
<br>
<br>

## **Spanning Tree:**
It is a sub graph of a unidirected connected graph, which includes all the vertices with minimum edges.<br>
Total number of spanning trees with `n` vertices are `n^(n-2)`.
<br>

### Example:
Original graph:-

<img src="https://cdn.programiz.com/sites/tutorial2program/files/initial-tree-mst_0_1.png" height="30%" width="30%">

Possible Spanning trees:-
<div display="flex">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/spanning-tree-1_0.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/spanning-tree-2_0.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/spanning-tree-3_0.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/spanning-tree-4_0.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/spanning-tree-5_0.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/spanning-tree-6_0.png" height="30%" width="30%">
</div>
<br>

### Applications:
- Computer network routing protocol
- Cluster analysis
- Civil network planning

****************************************************************************
<br>
<br>

## **Minimum Spanning Tree:**
It is a spanning tree in which sum of weights of the edges is as minimum as possible.
<br>

### Example:
Original graph:-
    
<img src="https://cdn.programiz.com/sites/tutorial2program/files/initial-tree-mst_0_1.png" height="30%" width="30%">

Possible Spanning trees:-
<div display="flex">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/mst-1_0_1.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/mst-2_0_1.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/mst-3_0_1.png" height="30%" width="30%">
<img src="https://cdn.programiz.com/sites/tutorial2program/files/mst-4_0_1.png" height="30%" width="30%">

Minimum Spanning tree:-

<img src="https://cdn.programiz.com/sites/tutorial2program/files/mst-2_0_1.png" height="30%" width="30%">
</div>
<br>

### Applications:
- Prim's Algorithm
- Kruskal's Algorithm
- Find paths in map
- Design networks like telecom network, water pipeline network and electrical grid.

****************************************************************************
<br>
<br>

## **Strongly Connected Components:**
It is a portion of directed graph in which all vertices are connected through a path.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/scc-strongly-connected-components.png" height="50%" width="50%">

### Kosaraju's Algorithm:
- Based on dfs implemented twice.
- 3 major steps:
    1. Perform dfs on whole graph.<br>
    Start from vertex-0 and visit all its child vertices and mark them as done. If any vertex leads to a visited vertex then push that vertex in a stack.
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/scc-step-1.png" height="50%" width="50%">
    <br>
    Go to the previous vertex and visit its child vertex, (i.e vertex-4, vertex-5, etc). If there is no vertex to move forward (i.e vertex-7), push it in stack and move to previous vertex and repeat.    
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/scc-step-4.png" height="50%" width="50%">    
    
    2. Reverse the original graph.
        
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/scc-reversed-graph.png" height="50%" width="50%">
    
    3. Perform dfs on reversed graph.<br>
    Start from top vertex of stack and visit all its child nodes. Once we reach an already visited node, one strongly connected component is found.
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/scc-reversed-step-1.png" height="50%" width="50%">
    <br>
    Go to the stack and pop the top vertex if already visited else, choose the vertex and traverse through child vertices as above.  
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/reversed%20step-2_0.png" height="50%" width="50%">
<br>

### Implementation
```python
# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()
```
<br>

### Complexity:
Kosaraju's algorithm runs in linear time i.e. `O(V+E)`.
<br>

### Applications:
- Vehicle routing applications.
- Maps
- Model-checking in formal verification

****************************************************************************
<br>
<br>

## **Adjacency Matrix:**
Its is a way of representing graphs using matrix of booleans.

### Pros:
- Adding/Removing edge, checking whether edge between to vertex exists is very time efficient (constant time).
- Advances in hardware enables us to perform expensive matrix operations on GPU.
- Good choice for dense graph.
<br>

## Cons:
- Requires a lot of space, V*v size.
- Expensive to perform operations like, `inEdges` and `outEdges`.
<br>

### Implementation:
```python
# Adjacency Matrix representation in Python


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()


if __name__ == '__main__':
    main()
```
<br>

### Applications:
- Creating routing table in networks.
- Navigation tasks

****************************************************************************
<br>
<br>

## **Adjacency List:**
It represents graphs as array of linked list.<br>
The index in the array represents a vertex and each element in its linked list represents the vertices that forms edge with the vertex.<br>
It is very efficient in terms of space.

### Structure:
The simplest adjacency list needs a node data structure to store a vertex and a graph data structure to organize the nodes.
```
struct node
{
    int vertex;
    struct node* next;
};

struct Graph
{
    int numVertices;
    struct node** adjLists;
};
```

### Implementation:
```python
# Adjascency List representation in Python


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
```

****************************************************************************
<br>
<br>

## **Depth First Search:**
Used for searching all the vertices of graph or tree.<br>
DFS puts vertices in 2 categories: visited and not visited.<br>
Purpose is to visit all nodes, avoiding cycles.

### Algorithm:
1. Put any one element of graph at the top of the stack.
2. Take the top element of stack and add to the visited list.
3. Create a list of vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
4. Keep repeating 2. and 3. untill stack is empty.

### Implementation:
```python
# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')
```
<br>

### Complexities:
Time Complexity: `O(V+E)`<br>
where `V` is number of nodes and `E` is edges.<br>
Space Complexity: `O(V)`
<br>

### Application:
- Find a path.
- Test if graph is biparite.
- Find strongly connected components.
- Detecting cycles in graph.

****************************************************************************
<br>
<br>

## **Breadth First Search:**
Used for searching all the vertices of graph or tree.<br>
BFS puts vertices in 2 categories: visited and not visited.<br>
Purpose is to visit all nodes, avoiding cycles.

### Algorithm:
1. Put any one element of graph at the back of the queue.
2. Take the front element of queue and add to the visited list.
3. Create a list of vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
4. Keep repeating 2. and 3. untill queue is empty. 
<br>

### Implementation:
```python
import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
```
<br>

### Complexities:
Time Complexity: `O(V+E)`<br>
where `V` is number of nodes and `E` is edges.<br>
Space Complexity: `O(V)`
<br>

### Application:
- Build index by search index.
- GPS navigation.
- Path finding algorithm.
- Forf-Fulkerson algorithm.
- Cycle detection.
- min spanning trees.

****************************************************************************
<br>
<br>

## **Bellman Ford's Algorithm:**
Helps in finding shortest path from a vertex to all other vertices of a weighted graph.<br>
Similar to Dijkstra's algorithm but works with graphs having negative weights.
<br>

### Importance of negative weights:
- Negative weights possible in phenomenas like cashflow or chemical reactions evolving heat dissipation or absorption.
- Negative weights can create negative cycle, which reduces total path distance by coming back to same point.
<br>

### Algorithm:
Works by overestimating the length of path from the starting vertex to all the vertices. Then it itratively relaxes those estimates by finding new paths which are shorter than the previously overestimated path.

```
function bellmanFord(G, S)
  for each vertex V in G
    distance[V] <- infinite
      previous[V] <- NULL
  distance[S] <- 0

  for each vertex V in G				
    for each edge (U,V) in G
      tempDistance <- distance[U] + edge_weight(U, V)
      if tempDistance < distance[V]
        distance[V] <- tempDistance
        previous[V] <- U

  for each edge (U,V) in G
    If distance[U] + edge_weight(U, V) < distance[V}
      Error: Negative Cycle Exists

  return distance[], previous[]
```
<br>

### Bellman Ford vs Dijkstra:
Dijkstra looks only at immediate neighbours of a vertex, Bellman Ford goes though each edge in every iteration.     
<img src="https://cdn.programiz.com/sites/tutorial2program/files/bellman-ford-vs-dijkstra.jpg" >
<br>

### Implementation:
```python
# Bellman Ford Algorithm in Python


class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)
```
<br>

### Complexities:
- **TIME**:
    Case | Complexity
    -----|-----------
    Best Case | O(E)
    Average Case | O(VE)
    Worst Case | O(VE)
- **SPACE**: O(V)
<br>

### Applications:
- Calculating shortest path in routing algorithm.
- Finding shorted path.

****************************************************************************
<br>
<br>

