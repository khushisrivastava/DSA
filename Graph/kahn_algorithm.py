from collections import deque
from graph import Graph

class Kahn(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.in_degree = {}

    def kahn(self):
        if not self.in_degree:
            self.in_degree = {i:0 for i in self.vertices}
        
        for i in self.vertices:
            for j in self.graph[i]:
                self.in_degree[j] += 1

        queue = deque()
        for i, val in self.in_degree.items():
            if val == 0:
                queue.append(i)
        
        res = []
        cnt = 0
        while queue:
            u = queue.popleft()
            res.append(u)

            for v in self.graph[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    queue.append(v)
            cnt += 1
        
        if cnt != len(self.vertices):
            print("Graph is cyclic")
        else:
            print(res)
                