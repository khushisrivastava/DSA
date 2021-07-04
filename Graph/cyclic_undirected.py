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

    def union_find(self):
        self.visited = set()

        for i in self.vertices:
            if i not in self.visited:
                if not self.parent:
                    self.parent = {i:i for i in self.vertices}
                self.visited.add(i)
                
                for nei in self.graph[i]:
                    if nei not in self.visited:
                        if self.find(i) == self.find(nei):
                            return True
                        self.union(self.find(i), self.find(nei))
        return False

    def dfs(self, node, parent):
        self.visited.add(node)

        for nei in self.graph[node]:
            if nei not in self.visited:
                if self.dfs(nei, node):
                    return True
            elif parent != nei:
                return True
        return False

    def is_cyclic_dfs(self):
        self.visited = set()
        
        for i in self.vertices:
            if i not in self.visited and self.dfs(i, -1):
                return True
        return False

    def bfs(self, node):
        self.parent = {i:i for i in self.vertices}
        self.visited.add(node)

        queue = deque()
        queue.append(node)

        while queue:
            v = queue.popleft()

            for nei in self.graph[v]:
                if nei not in self.visited:
                    self.visited.add(nei)
                    queue.append(nei)
                    self.parent[nei] = v

                elif self.parent[v] != nei: 
                    return True
        return False

    def is_cyclic_bfs(self):
        self.visited = set()

        for i in self.vertices:
            if i not in self.visited and self.bfs(i):
                return True
        return False
