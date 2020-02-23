from graph import Graph
from queue import Queue
import sys
def breth_first(graph,start_vertex):
	q=Queue()
	visited=[]
	q.put(start_vertex)
	visited.append(start_vertex)
	while not q.empty():
		current_vertex=q.get()
		print(current_vertex)
		for v in graph.get_adjacency_list(current_vertex):
			if v not in visited:
				q.put(v)
				visited.append(v)
	print(visited)


g=Graph(8)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(3,5)
g.add_edge(0,4)
g.add_edge(4,6)
g.add_edge(2,7)

breth_first(g,0)