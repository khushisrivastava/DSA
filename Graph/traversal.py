from graph import Graph
from collections import deque

class Traversal(Graph):
    def bfs(self, node):
        visited = {node}
        queue = deque([node])

        while queue:
            node = queue.popleft()
            print(f"{node} -> ", end="")

            for v in self.graph[node]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

    def __init__(self) -> None:
        self.visited = set()
        super().__init__()

    def dfs(self, node, visited=None):
        if not visited:
            visited = set()
        
        visited.add(node)
        print(f"{node} -> ", end="")
        for v in self.graph[node]:
            if v not in visited:
                self.dfs(v, visited)
