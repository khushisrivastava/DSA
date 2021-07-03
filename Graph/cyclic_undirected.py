from graph import Graph
from collections import deque

class Cyclic(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.visited = set()
        self.parent = {}
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, src, dest):
        self.parent[dest] = src

    def dfs(self, node):
        if not self.parent:
            self.parent = {i:i for i in self.vertices}
        self.visited.add(node)
        
        for nei in self.graph[node]:
            if nei not in self.visited:
                if self.find(node) == self.find(nei):
                    return True
                self.union(self.find(node), self.find(nei))

    def bfs(self, node):
        if not self.parent:
            self.parent = {i:i for i in self.vertices}
        self.visited.add(node)

        queue = deque([node])
        while queue:
            src = queue.popleft()

            for nei in self.graph[src]:
                if nei not in self.visited:
                    queue.append(nei)
                    self.visited.add(nei)
                    if self.find(node) == self.find(nei):
                        return True
                    self.union(self.find(node), self.find(nei))
        return False
