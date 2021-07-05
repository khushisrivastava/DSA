from graph import Graph

class BellmanFord(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.weight = {}

    def maintain_graph(self):
        res = []
        for key in self.graph:
            for nei in self.graph[key]:
                res.append([key, nei[0], nei[1]])
        return res
    
    def bellman_ford(self, src):
        if not self.weight:
            self.weight = {i:float("inf") for i in self.vertices}
            self.weight[src] = 0
            new_graph = self.maintain_graph()

            for _ in range(len(self.vertices)-1):
                for u,v,w in new_graph:
                    if self.weight[u] != float("inf") and (new_weight := self.weight[u] + w) < self.weight[v]:
                        self.weight[v] = new_weight
            
            for u,v,w in new_graph:
                if self.weight[u] != float("inf") and (new_weight := self.weight[u] + w) < self.weight[v]:
                    print("Graph contains a negative cycle")
                    return
            
            print("Distance of vertices from source: ")
            for i in self.vertices:
                print(f"{i} -> {self.weight[i]} units")
