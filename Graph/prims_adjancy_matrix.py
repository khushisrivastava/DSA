class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]
        self.parent = {}
        self.visited = set()

    def get_min(self, weight):
        min_weight = float("inf")
        for v in range(self.V):
            if weight[v] < min_weight and v not in self.visited:
                min_weight = weight[v]
                min_index = v
        return min_index
        

    def prims(self, root):
        weight = {i: float("inf") for i in range(self.V)}
        weight[root] = 0
        self.parent[root] = None

        for i in range(self.V):
            source = self.get_min(weight)
            self.visited.add(source)

            for dest in range(self.V):
                if dest not in self.visited and self.graph[source][dest] > 0 and weight[dest] > self.graph[source][dest]:
                    self.parent[dest] = source
                    weight[dest] = self.graph[source][dest]

        print("Edges in Minimum Spanning Tree are:")
        del self.parent[root]
        for src, dest in self.parent.items():
            print(f"{dest} -> {src}")

        