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

