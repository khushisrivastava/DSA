class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]
        self.visited = set()

    def get_min_weight(self, weight):
        min_weight = float("inf")
        for i in range(self.V):
            if i not in self.visited and weight[i] < min_weight:
                min_weight = weight[i]
                min_index = i
        return min_index

    def dijkstra(self, node):
        weight = {i: float("inf") for i in range(self.V)}
        weight[node] = 0

        for _ in range(self.V):
            source = self.get_min_weight(weight)
            self.visited.add(source)
            
            for dest in range(self.V):
                if dest not in self.visited and self.graph[source][dest] > 0 and weight[source] + self.graph[source][dest] < weight[dest]:
                    weight[dest] = self.graph[source][dest] + weight[source]

        print("Distance of vertices from source: ")
        for i, weight in weight.items():
            print(f"{i} -> {weight} units")
 