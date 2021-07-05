class FloydWarshall():
    def __init__(self, vertex) -> None:
        self.V = vertex
        self.graph = [[0 for col in range(vertex)] for row in range(vertex)]
    
    def floyd_warshall(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.graph[i][k] == -1 or self.graph[k][j] == -1:
                        continue
                    elif self.graph[i][j] == -1:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]
                    else:
                        self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
        
        print("Shorted distance between each pair of vertices")
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end=" ")
                if j == self.V-1:
                    print()

g = FloydWarshall(4)
g.graph = [[0, 5, -1, 10],
        [-1, 0, 3, -1],
        [-1, -1, 0,   1],
        [-1, -1, -1, 0]
    ]
g.floyd_warshall()
