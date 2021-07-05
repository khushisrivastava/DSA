from graph import Graph

class Node:
    def __init__(self, vertex, weight) -> None:
        self.vertex = vertex
        self.weight = weight

class Heaps:
    def __init__(self) -> None:
        self.array = []
        self.pos = {}

    def is_empty(self):
        return len(self.array) == 0

    def swap_pos(self, p1, p2):
        self.pos[p1], self.pos[p2] = self.pos[p2], self.pos[p1]
    
    def swap_nodes(self, n1, n2):
        self.array[n1], self.array[n2] = self.array[n2], self.array[n1]

    def heapify(self, index):
        smallest = index
        left = (2 * index) + 1
        right = (2 * index) + 2

        if left < len(self.array) and self.array[left].weight < self.array[smallest].weight:
            smallest = left

        if right < len(self.array) and self.array[right].weight < self.array[smallest].weight:
            smallest = right
        
        if smallest != index:
            self.swap_pos(self.array[smallest].vertex, self.array[index].vertex)
            self.swap_nodes(smallest, index)
            self.heapify(smallest)

    def extract_min(self):
        if self.is_empty():
            return
        root = self.array[0]
        del self.pos[root.vertex]

        if len(self.array) > 1:
            self.array[0] = self.array.pop()
            self.pos[self.array[0].vertex] = 0
            self.heapify(0)
        else:
            self.array.pop()

        return root

    def is_in_heap(self, node):
        return node in self.pos

    def update_weight(self, vertex, weight):
        index = self.pos[vertex]
        self.array[index].weight = weight

        while index > 0 and self.array[index].weight < self.array[int((index-1)/2)].weight:
            self.swap_pos(self.array[index].vertex, self.array[int((index-1)/2)].vertex)
            self.swap_nodes(index, int((index-1)/2))

            index = int((index-1)/2)

class Prims(Graph):
    def prims(self, root):
        weight = {i:float("inf") for i in self.vertices}
        weight[root] = 0

        parent = {root: None}
        heap = Heaps()

        for i, vertex in enumerate(self.vertices):
            heap.array.append(Node(vertex, weight[vertex]))
            heap.pos[vertex] = i
        
        while not heap.is_empty():
            source = heap.extract_min()

            for nei in self.graph[source.vertex]:
                if heap.is_in_heap(nei[0]) and nei[1] < weight[nei[0]]:
                    weight[nei[0]] = nei[1]
                    parent[nei[0]] = source.vertex
                    heap.update_weight(nei[0], nei[1])

        print("Edges in Minimum Spanning Tree are:")
        del parent[root]
        for src, dest in parent.items():
            print(f"{dest} -> {src}")