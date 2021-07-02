from graph import Graph
from collections import deque

class BFS(Graph):
    def bfs(self, node):
        visited = {0}
        queue = deque([node])

        while queue:
            node = queue.popleft()
            print(f"{node} -> ")

            for v in self.graph[node]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

