from graph import Graph

def depth_first(graph,current_vertex,visited=[]):
	if current_vertex in visited:
		return
	visited.append(current_vertex)

	for v in graph.get_adjacency_list(current_vertex):
		print(v)
		if v not in visited:
			depth_first(graph,v,visited)


g=Graph(8)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(3,5)
g.add_edge(0,4)
g.add_edge(4,6)
g.add_edge(2,7)

visited=[]

depth_first(g,0,visited)
print(visited)