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
        return False if self.array else True
    
    def swap_pos(self, v1, v2):
        self.pos[v1], self.pos[v2] = self.pos[v2], self.pos[v1]
    
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

    def is_in_min_heap(self, vertex):
        return vertex in self.pos

    def update_weight(self, vertex, weight):
        index = self.pos[vertex]
        self.array[index].weight = weight
        while index > 0 and self.array[index].weight < self.array[int((index - 1) / 2)].weight:
            self.swap_nodes(index, int((index - 1) / 2))
            self.swap_pos(self.array[index].vertex, self.array[int((index - 1) / 2)].vertex)
            index = int((index - 1) / 2)

class Dijktra(Graph):
    def dijkstra(self, src):
        weight = {i:float("inf") for i in self.vertices}
        weight[src] = 0

        heap = Heaps()
        for i, v in enumerate(self.vertices):
            heap.array.append(Node(v, weight[v]))
            heap.pos[v] = i
        
        while not heap.is_empty():
            source = heap.extract_min()

            for nei in self.graph[source.vertex]:
                if heap.is_in_min_heap(nei[0]) and weight[source.vertex] != float("inf") and nei[1] + weight[source.vertex] < weight[nei[0]]:
                    weight[nei[0]] = nei[1] + weight[source.vertex]
                    heap.update_weight(nei[0], weight[nei[0]])
        
        print("Distance of vertices from source: ")
        for i in self.vertices:
            print(f"{i} -> {weight[i]} units")