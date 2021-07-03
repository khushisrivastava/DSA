from graph import Graph
from collections import deque, defaultdict

class Cyclic(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.visited = set()

    def dfs(self, node, path=set()):
        path.add(node)
        self.visited.add(node)

        for v in self.graph[node]:
            if v not in self.visited:
                if self.dfs(v, path):
                    return True
            elif v in path:
                return True
        path.remove(node)
        return False
    
    def bfs(self):
        in_degree = defaultdict(int, {k:0 for k in self.vertices})
        
        for i in self.vertices:
            for j in self.graph[i]:
                in_degree[j] += 1
        
        count = 0
        queue = deque()
        for i in in_degree:
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            v = queue.popleft()
            for nei in self.graph[v]:
                in_degree[nei] -= 1

                if in_degree[nei] == 0:
                    queue.append(nei)
            count += 1
        
        if count == len(self.vertices):
            return False
        return True
