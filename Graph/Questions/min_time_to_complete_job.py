from collections import defaultdict, deque
 
class Graph:
     
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.n = vertices 
        self.in_degree = {i:0 for i in vertices}
        self.job = {i:0 for i in vertices}

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def time(self):
        for i in self.n:
            for j in self.graph[i]:
                self.in_degree[j] += 1

        queue = deque()
        for i in self.in_degree:
            if self.in_degree[i] == 0:
                queue.append(i)
                self.job[i] = 1
        
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                self.in_degree[v] -= 1

                if self.in_degree[v] == 0:
                    queue.append(v)
                    self.job[v] = 1 + self.job[u]
        
        print(*self.job.values())

g = Graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 6)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 10)
g.time()