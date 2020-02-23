from graph import Graph
from queue import Queue

def construct_distance_table(graph,start_v):
	distance_table={}# {vertex,(distance,predecessor)}
	q=Queue()

	for v in range(graph.numVertex):
		distance_table[v]=(None,None)
	q.put(start_v)
	distance_table[start_v]=(0,None)
	print(distance_table)


	while not q.empty():
		current_vertex=q.get()
		current_distance=distance_table[current_vertex][0]


		for v in graph.get_adjacency_list(current_vertex):
			if distance_table[v][0] is None:
				distance_table[v]=(current_distance+1,current_vertex)
				q.put(v)
	return distance_table




def find_shortest_path(graph,start_v,end_v):
	distance_table=construct_distance_table(graph,start_v)
	current_vertex=end_v
	shortest_path=[]
	while current_vertex!=start_v:
		shortest_path=[current_vertex]+shortest_path
		current_vertex=distance_table[current_vertex][1]

	shortest_path=[start_v]+shortest_path

	print(shortest_path)









g=Graph(9)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(3,5)
g.add_edge(0,4)
g.add_edge(4,6)
g.add_edge(2,7)
g.add_edge(7,8)
g.add_edge(0,8)


#construct_distance_table(g,0)

find_shortest_path(g,0,8)

