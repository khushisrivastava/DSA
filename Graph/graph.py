from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.vertices = set()
        self.graph = defaultdict(list, {k:[] for k in self.vertices})
    
    def add_node_undirected(self, src, dest) -> None:
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def add_node_weighted_undirected(self, src, dest, wei) -> None:
        self.graph[src].append((dest, wei))
        self.graph[dest].append((src, wei))
    
    def add_node_directed(self, src, dest) -> None:
        self.graph[src].append(dest)
    
    def print_graph(self) -> None:
        for k, v in self.graph.items():
            print(f"{k} -> ", *v)

