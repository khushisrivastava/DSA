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

### Cons:
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

## **Kruskal's Algorithm:**
It is the algorithm which takes graphs as input and returns minimum spanning tree as output.

### Algorithm:
Falls under greedy algorithm, that finds local optimum to find global minimum.<br>
Kruskal's algorithm sorts all the edges from low weight to high and keeps adding the lowest edges, ignoring those edges that create a cycle.<br>
For a graph having `N` vertices, spanning tree should have total `N-1` edges.
1. Sort all the edges in acending order of weights.
2. Take the edge with lowest weight and add it to the spanning tree. If adding creates cycle, reject it.
3. Keep adding edges untill we reach all the edges.

The algorithm revolves around whether adding an edge created a loop of not.<br>
This can be done using an algorithm `Union Find`. It divides vertices into clusters and checks if two vertices belong to same cluster or not.

```
KRUSKAL(G):
A = ∅
For each vertex v ∈ G.V:
    MAKE-SET(v)
For each edge (u, v) ∈ G.E ordered by increasing order by weight(u, v):
    if FIND-SET(u) ≠ FIND-SET(v):       
    A = A ∪ {(u, v)}
    UNION(u, v)
return A
```
<br>

### Implementation:
```python
# Kruskal's algorithm in Python


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        return parent[i]

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()
```
<br>

### Complexity:
Time complexity is `O(E logE)`<br>
`E` is number of edges.
<br>

### Application:
- Layout electrical wiring.
- LAN connection.

****************************************************************************
<br>
<br>

## **Prim's Algorithm**
It is the algorithm which takes graphs as input and returns minimum spanning tree as output.

### Algorithm:
Prim's algorithm starts from a vertex and keeps adding lowest-weight edges which aren't in the tree, until all vertices have been covered.<br>
Number of edges in minimum spanning tree is always `<= V-1`.
1. Initialize minimum spanning tree with a vertex choosen at random.
2. Find all the edges that connects the vertex with other vertices, find thee minimum and add to the tree.
3. Keep repeating untill all the nodes are covered.

The algorithm containes 2 sets `U` and `V-U`. `U` contains the nodes we have visited and `V-U` contains the one we haven't. 
```
T = ∅;
U = { 1 };
while (U ≠ V)
    let (u, v) be the lowest cost edge such that u ∈ U and v ∈ V - U;
    T = T ∪ {(u, v)}
    U = U ∪ {v}
```
<br>

### Implementation for Adjacency Matrix:
```python
# Prim's Algorithm in Python


INF = 9999999
# number of vertices in graph
V = 5
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
```
<br>
<br>

```python
import sys # Library for INT_MAX
  
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
  
    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print "Edge \tWeight"
        for i in range(1, self.V):
            print parent[i], "-", i, "\t", self.graph[i][ parent[i] ]
  
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
  
        # Initilaize min value
        min = sys.maxint
  
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
  
        return min_index
  
    # Function to construct and print MST for a graph 
    # represented using adjacency matrix representation
    def primMST(self):
  
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxint] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0 
        mstSet = [False] * self.V
  
        parent[0] = -1 # First node is always the root of
  
        for cout in range(self.V):
  
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
  
            # Put the minimum distance vertex in 
            # the shortest path tree
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
  
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
  
        self.printMST(parent)
  
g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
  
g.primMST();
```
<br>

### Implementation for Adjacency List:
```python
# A Python program for Prims's MST for
# adjacency list representation of graph

from collections import defaultdict
import sys

class Heap():

	def __init__(self):
		self.array = []
		self.size = 0
		self.pos = []

	def newMinHeapNode(self, v, dist):
		minHeapNode = [v, dist]
		return minHeapNode

	# A utility function to swap two nodes of
	# min heap. Needed for min heapify
	def swapMinHeapNode(self, a, b):
		t = self.array[a]
		self.array[a] = self.array[b]
		self.array[b] = t

	# A standard function to heapify at given idx
	# This function also updates position of nodes
	# when they are swapped. Position is needed
	# for decreaseKey()
	def minHeapify(self, idx):
		smallest = idx
		left = 2 * idx + 1
		right = 2 * idx + 2

		if left < self.size and self.array[left][1] < \
								self.array[smallest][1]:
			smallest = left

		if right < self.size and self.array[right][1] < \
								self.array[smallest][1]:
			smallest = right

		# The nodes to be swapped in min heap
		# if idx is not smallest
		if smallest != idx:

			# Swap positions
			self.pos[ self.array[smallest][0] ] = idx
			self.pos[ self.array[idx][0] ] = smallest

			# Swap nodes
			self.swapMinHeapNode(smallest, idx)

			self.minHeapify(smallest)

	# Standard function to extract minimum node from heap
	def extractMin(self):

		# Return NULL wif heap is empty
		if self.isEmpty() == True:
			return

		# Store the root node
		root = self.array[0]

		# Replace root node with last node
		lastNode = self.array[self.size - 1]
		self.array[0] = lastNode

		# Update position of last node
		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1

		# Reduce heap size and heapify root
		self.size -= 1
		self.minHeapify(0)

		return root

	def isEmpty(self):
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist):

		# Get the index of v in heap array

		i = self.pos[v]

		# Get the node and update its dist value
		self.array[i][1] = dist

		# Travel up while the complete tree is not
		# hepified. This is a O(Logn) loop
		while i > 0 and self.array[i][1] < \
					self.array[(i - 1) / 2][1]:

			# Swap this node with its parent
			self.pos[ self.array[i][0] ] = (i-1)/2
			self.pos[ self.array[(i-1)/2][0] ] = i
			self.swapMinHeapNode(i, (i - 1)/2 )

			# move to parent index
			i = (i - 1) / 2;

	# A utility function to check if a given vertex
	# 'v' is in min heap or not
	def isInMinHeap(self, v):

		if self.pos[v] < self.size:
			return True
		return False


def printArr(parent, n):
	for i in range(1, n):
		print "% d - % d" % (parent[i], i)


class Graph():

	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	# Adds an edge to an undirected graph
	def addEdge(self, src, dest, weight):

		# Add an edge from src to dest. A new node is
		# added to the adjacency list of src. The node
		# is added at the beginning. The first element of
		# the node has the destination and the second
		# elements has the weight
		newNode = [dest, weight]
		self.graph[src].insert(0, newNode)

		# Since graph is undirected, add an edge from
		# dest to src also
		newNode = [src, weight]
		self.graph[dest].insert(0, newNode)

	# The main function that prints the Minimum
	# Spanning Tree(MST) using the Prim's Algorithm.
	# It is a O(ELogV) function
	def PrimMST(self):
		# Get the number of vertices in graph
		V = self.V
		
		# key values used to pick minimum weight edge in cut
		key = []
		
		# List to store contructed MST
		parent = []

		# minHeap represents set E
		minHeap = Heap()

		# Initialize min heap with all vertices. Key values of all
		# vertices (except the 0th vertex) is is initially infinite
		for v in range(V):
			parent.append(-1)
			key.append(sys.maxint)
			minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) )
			minHeap.pos.append(v)

		# Make key value of 0th vertex as 0 so
		# that it is extracted first
		minHeap.pos[0] = 0
		key[0] = 0
		minHeap.decreaseKey(0, key[0])

		# Initially size of min heap is equal to V
		minHeap.size = V;

		# In the following loop, min heap contains all nodes
		# not yet added in the MST.
		while minHeap.isEmpty() == False:

			# Extract the vertex with minimum distance value
			newHeapNode = minHeap.extractMin()
			u = newHeapNode[0]

			# Traverse through all adjacent vertices of u
			# (the extracted vertex) and update their
			# distance values
			for pCrawl in self.graph[u]:

				v = pCrawl[0]

				# If shortest distance to v is not finalized
				# yet, and distance to v through u is less than
				# its previously calculated distance
				if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
					key[v] = pCrawl[1]
					parent[v] = u

					# update distance value in min heap also
					minHeap.decreaseKey(v, key[v])

		printArr(parent, V)


# Driver program to test the above functions
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.PrimMST()
```
<br>

### Complexity:
Time complexity is `O(E logV)` for adjancy list and `O(V^2)` for adjancy matrix.<br>
`E` is number of edges and `V` is number of vertices.
<br>

### Application:
- Laying cables for electrical wiring.
- Network design
- Make protocols in network cycles.

****************************************************************************
<br>
<br>

## **Dijkstra's Algorithm:**
It is used to find shortest path between 2 vetrices. 

### Algorithm:
Any subpath `B->D` of shortest path `A->D` between vertices `A` and `D` is also the shortes path between `B` and `D`.<br>
We overestimate the distance of each vertex from the starting vertex. Then we visit each node and its neighbors to find the shortest subpath to those neighbors.
```
function dijkstra(G, S)
    for each vertex V in G
        distance[V] <- infinite
        previous[V] <- NULL
        If V != S, add V to Priority Queue Q
    distance[S] <- 0
	
    while Q IS NOT EMPTY
        U <- Extract MIN from Q
        for each unvisited neighbour V of U
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]
                distance[V] <- tempDistance
                previous[V] <- U
    return distance[], previous[]
```
<br>

### Implementation using Adjancy Matrix:
```python
# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph
  
# Library for INT_MAX
import sys
  
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
  
    def printSolution(self, dist):
        print "Vertex \tDistance from Source"
        for node in range(self.V):
            print node, "\t", dist[node]
  
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
  
        # Initilaize minimum distance for next node
        min = sys.maxint
  
        # Search not nearest vertex not in the 
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
  
        return min_index
  
    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation
    def dijkstra(self, src):
  
        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
  
        for cout in range(self.V):
  
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
  
            # Put the minimum distance vertex in the 
            # shotest path tree
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
  
        self.printSolution(dist)
  
# Driver program
g = Graph(9)
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
```
<br>

### Implementation using Adjancy List:
```python
# A Python program for Dijkstra's shortest
# path algorithm for adjacency
# list representation of graph
 
from collections import defaultdict
import sys
 
class Heap():
 
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []
 
    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode
 
    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMinHeapNode(self,a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t
 
    # A standard function to heapify at given idx
    # This function also updates position of nodes
    # when they are swapped.Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
 
        if left < self.size and
           self.array[left][1] \
            < self.array[smallest][1]:
            smallest = left
 
        if right < self.size and
           self.array[right][1]\
            < self.array[smallest][1]:
            smallest = right
 
        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:
 
            # Swap positions
            self.pos[ self.array[smallest][0]]
                                       = idx
            self.pos[ self.array[idx][0]] =
                                     smallest
 
            # Swap nodes
            self.swapMinHeapNode(smallest, idx)
 
            self.minHeapify(smallest)
 
    # Standard function to extract minimum
    # node from heap
    def extractMin(self):
 
        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return
 
        # Store the root node
        root = self.array[0]
 
        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
 
        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
 
        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)
 
        return root
 
    def isEmpty(self):
        return True if self.size == 0 else False
 
    def decreaseKey(self, v, dist):
 
        # Get the index of v in  heap array
 
        i = self.pos[v]
 
        # Get the node and update its dist value
        self.array[i][1] = dist
 
        # Travel up while the complete tree is
        # not hepified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] <
                  self.array[(i - 1) / 2][1]:
 
            # Swap this node with its parent
            self.pos[ self.array[i][0] ] = (i-1)/2
            self.pos[ self.array[(i-1)/2][0] ] = i
            self.swapMinHeapNode(i, (i - 1)/2 )
 
            # move to parent index
            i = (i - 1) / 2;
 
    # A utility function to check if a given
    # vertex 'v' is in min heap or not
    def isInMinHeap(self, v):
 
        if self.pos[v] < self.size:
            return True
        return False
 
 
def printArr(dist, n):
    print "Vertex\tDistance from source"
    for i in range(n):
        print "%d\t\t%d" % (i,dist[i])
 
 
class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
 
    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):
 
        # Add an edge from src to dest.  A new node
        # is added to the adjacency list of src. The
        # node is added at the beginning. The first
        # element of the node has the destination
        # and the second elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)
 
        # Since graph is undirected, add an edge
        # from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)
 
    # The main function that calulates distances
    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def dijkstra(self, src):
 
        V = self.V  # Get the number of vertices in graph
        dist = []   # dist values used to pick minimum
                    # weight edge in cut
 
        # minHeap represents set E
        minHeap = Heap()
 
        #  Initialize min heap with all vertices.
        # dist value of all vertices
        for v in range(V):
            dist.append(sys.maxint)
            minHeap.array.append( minHeap.
                                newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)
 
        # Make dist value of src vertex as 0 so
        # that it is extracted first
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])
 
        # Initially size of min heap is equal to V
        minHeap.size = V;
 
        # In the following loop,
        # min heap contains all nodes
        # whose shortest distance is not yet finalized.
        while minHeap.isEmpty() == False:
 
            # Extract the vertex
            # with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
 
            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:
 
                v = pCrawl[0]
 
                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if minHeap.isInMinHeap(v) and
                     dist[u] != sys.maxint and \
                   pCrawl[1] + dist[u] < dist[v]:
                        dist[v] = pCrawl[1] + dist[u]
 
                        # update distance value
                        # in min heap also
                        minHeap.decreaseKey(v, dist[v])
 
        printArr(dist,V)
 
 
# Driver program to test the above functions
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)
```
<br>

### Complexity:
Time complexity is `O(E logV)` for adjancy list and `O(V^2)` for adjancy matrix.<br>
`E` is number of edges and `V` is number of vertices.
<br>

### Application:
- To find shortest path
- Social networking application
- telephone network
- Find location on map

***************************************************************************
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

## **Floyd Warshall's Algorithm:**
It is used to find shorted distance between all pair of vertices in a weighted graph. It works for both directed and unidirected graph but not for graph having negative cycle.<br>
It used dynamc approach to find shortest path.

### Algorithm:
1. Create a matrix `A0` and fill each cell with the weights. Fill with `INF` if there is no path between 2 vertex.
2. Create a matrix `A1` using `A0`. Keep 1st row and column as it it and fill the remaining as: `(A[i][k] + A[k][j]) if (A[i][j] > A[i][k] + A[k][j])`.<br>
In this step, `k=1`. We calculate the distance from source vertex to destination vertex through this vertex k.
3. Follow step `2` untill we have covered all the rows.<br>
The obtained matrix is the matrix with shortest path.

```
n = no of vertices
A = matrix of dimension n*n
for k = 1 to n
    for i = 1 to n
        for j = 1 to n
            Ak[i, j] = min (Ak-1[i, j], Ak-1[i, k] + Ak-1[k, j])
return A
```
<br>

### Implementation:
```python
# Floyd Warshall Algorithm in python


# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)
```
<br>

### Complexity:
- **Time**: O(n^3)
- **Space**: O(n^2)
<br>

### Application:
- Find shorted path in directed graph.
- Find transitive closure of directive graph.
- Find inversion of real matrix.
- Testing whether unidirected graph is bipartite.

***************************************************************************
<br>
<br>

## **Topological Sort:**
Topological sorting is only possible in Directed Acyclic Graph. It is a liner ordering of vertices such tha for every directed edge `(u,v)`, vertex `u` comes before vertex `v` in ordering.<br>
The first vertex of topological sort is always the vertex with in-order degree as 0.
<br>

### Implementation:
```python
# Python program to print topological sorting of a DAG
from collections import defaultdict
 
# Class to represent a graph
 
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
 
 
# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
 
# Function Call
g.topologicalSort()
```
<br>

### Complexity:
- Time: O(V+E)
- Space: O(V)
<br>

### Applications:
- Scheduling jobs

***************************************************************************
<br>
<br>

## **Kahn's Algorithm**
This algorithm is used to find topological sort of a graph.<br>
It is based on the idea that in a directed acyclic graph there is atleast 1 node with in-degree 0 and 1 node with out-degree 0.
<br>

### Algorithm:
- Compute in-degree for each node in the graph and initialise the count of visited node to 0.
- Pick all the nodes with in-degree 0 and push them in queue.
- Remove vertex from queue
    - Increment count of visited node to 1
    - Decrease in-degree of neighbouring nodes by 1
    - If in-degree of neighbouring node is 0, add them to queue.
    - Repeat untill queue is empty.
- If count of visited nodes is not equal to number of vertices, then topological sort is not possible.
<br>

### Implementation:
```python
# A Python program to print topological sorting of a graph
# using indegrees
from collections import defaultdict
  
# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.V = vertices # No. of vertices
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
  
    # The function to do Topological Sort. 
    def topologicalSort(self):
          
        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0]*(self.V)
          
        # Traverse adjacency lists to fill indegrees of
           # vertices.  This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
  
        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
  
        # Initialize count of visited vertices
        cnt = 0
  
        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []
  
        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:
  
            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)
  
            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)
  
            cnt += 1
  
        # Check if there was a cycle
        if cnt != self.V:
            print "There exists a cycle in the graph"
        else :
            # Print topological order
            print top_order
  
  
g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
  
print "Following is a Topological Sort of the given graph"
g.topologicalSort()
```
<br>

### Complexity:
- Time: O(V+E)
- Space: O(V)

***************************************************************************
<br>
<br>
