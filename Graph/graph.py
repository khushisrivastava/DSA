from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_node(self, src, dest) -> None:
        self.graph[src].append(dest)
        self.graph[dest].append(src)
    
    def print_graph(self) -> None:
        for k, v in self.graph.items():
            print(f"{k} -> ", *v)



