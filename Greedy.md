# <center>**Greedy**
<br>

These algorithms are based on the apprach that the current solutions is the best solution. It might not be the correct answer.<br>
It works in top-down approach. It goes for local best choise to produce global best result.
<br>

Greedy algo is used when problems have:
- **Greedy choice property**: If optimum solution can be found by choosing the best choice at each step.
- **Optimal substructure**: If overall optimal solutions of problem corresponds to optimal solution in each subproblem.

### Advantages:
- easy to describe
- performs better (in most cases)

### Drawbacks:
- Doesn't always produces an optimal solution

### Approach:
- Start with an empty set containing solution
- At each step, an item is added in the solution set
- If solution set is feasible, the current solution is kept else discarded and not considered again.

### Types:
- Selection Sort
- Knapsack Problem
- Minimum Spanning Tree
- Single source shortest path problem
- Job scheduling problem
- Prim's
- Krushkal's
- Dijkstra's
- Huffman's
- Ford-Fulkerson's

****************************************************************************
<br>
<br>

## **Ford-Fulkerson Algorithm**
It is used for calculating maximum possible flow in a graph.<br>
A term, flow network, is used to describe a network of vertices and edges with a source (S) and a sink (T). Each vertex, except S and T, can receive and send an equal amount of stuff through it. S can only send and T can only receive stuff.

### Terminology:
- Augmenting Path: Path available in a flow network.
- Residual Graph: Flow network that has additional possible flow.
- Residual Capacity: Capacity of the edge after subtracting the flow from the maximum capacity.
<br>

### Algorithm:
- Initialize the flow of each edge to 0.
- While there is an augmenting path between source and sink, add this path to flow.
- Updated residual graph.
<br>

### Implementation:
```python
from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Max Flow: %d " % g.ford_fulkerson(source, sink))
```
<br>

### Application:
- Water distribution pipeline
- Bipartite matching problem
- Circulation on demands

****************************************************************************
<br>
<br>

## **Huffman Algorithm**
It is a technique of compressing data to reduce its size witout any loss in the details.

### Implementation:
```python
# Huffman Coding in python

string = 'BCAADDDCCACACAC'


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
```
<br>

### Complexity:
- Encoding Character: O(n logn)
<br>

### Applications:
- Used in conventional compression formats like GZIP, BZIP2, PKZIP, etc.
- For text and fax transmission

****************************************************************************
<br>
<br>
