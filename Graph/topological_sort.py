from graph import Graph

class TopologicalSort(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.visited = set()
    
    def sort(self, vertex, stack):
        self.visited.add(vertex)
        for i in self.graph[vertex]:
            if i not in self.visited:
                self.sort(i, stack)
        stack.append(vertex)

    def topological_sort(self):
        stack = []

        for i in self.vertices:
            if i not in self.visited:
                self.sort(i, stack)
        
        print(stack[::-1])