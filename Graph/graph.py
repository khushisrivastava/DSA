from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.vertices = set()
        self.graph = defaultdict(list)
    
    def add_node_unidirected(self, src, dest) -> None:
        self.graph[src].append(dest)
        self.graph[dest].append(src)
    
    def add_node_directed(self, src, dest) -> None:
        self.graph[src].append(dest)
    
    def print_graph(self) -> None:
        for k, v in self.graph.items():
            print(f"{k} -> ", *v)

