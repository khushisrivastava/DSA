from graph import Graph
from bfs import BFS


g = Graph()
g.add_node(1, 3)
g.add_node(2, 3)
g.add_node(0, 4)
g.add_node(3, 4)
g.add_node(1, 2)
g.add_node(0, 1)
g.add_node(1, 4)
g.print_graph()

bfs = BFS()
bfs.bfs(1)