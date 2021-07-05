from graph import Graph

class Krushkal(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.parent = {}
        self.rank = {}
    
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, src, dest):
        if self.rank[src] < self.rank[dest]:
            self.parent[src] = dest
        elif self.rank[dest] < self.rank[src]:
            self.parent[dest] = src
        else:
            self.rank[src] += 1
            self.parent[dest] = src

    def maintain_graph(self):
        res = []
        for key in self.graph:
            for nei in self.graph[key]:
                res.append([key, nei[0], nei[1]])
        return res

    def kruskal(self):
        if not self.parent:
            self.parent = {i:i for i in self.vertices}
            self.rank = {i:0 for i in self.vertices}
        
        new_graph = self.maintain_graph()
        
        new_graph = sorted(new_graph, key=lambda item: item[2])
        result = []

        for edge in new_graph:
            x = self.find(edge[0])
            y = self.find(edge[1])

            if x != y:
                result.append([edge[0], edge[1], edge[2]])
                self.union(x, y)
        
        print("Edges in Minimum Spanning Tree are:")
        for src, dest, cost in result:
            print(f"{src} <-> {dest} : {cost}")
