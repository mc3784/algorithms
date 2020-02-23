import heapq
from graph import Graph


class PriorityEntry(object):

    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

def get_distance_table(graph,start_v):
	distance_table={}#{vertex:(distance,predecessor)}
	q=[]
	for v in range(graph.numVertex):
		distance_table[v]=(None,None)

	distance_table[start_v]=(0,None)
	heapq.heappush(q,PriorityEntry(0,start_v))

	while q:
		current=heapq.heappop(q)
		current_vertex=current.data
		current_distance=current.priority

		for v in graph.get_adjacency_list(current_vertex):
			new_distance=current_distance+graph.adjacencyMatrix[current_vertex][v]
			if distance_table[v][0] is None or distance_table[v][0]>new_distance:
				distance_table[v]=(new_distance,current_vertex)
				heapq.heappush(q,PriorityEntry(new_distance,v))
	return distance_table


def dijsktra(graph,start_v,end_v):
	distance_table=get_distance_table(graph,start_v)
	current_vertex=end_v
	shortest_path=[]
	while current_vertex!=start_v:
		shortest_path=[current_vertex]+shortest_path
		current_vertex=distance_table[current_vertex][1]
	shortest_path=[start_v]+shortest_path

	print(shortest_path)




g=Graph(8)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(3,5)
g.add_edge(0,4)
g.add_edge(4,6)
g.add_edge(2,7)
g.add_edge(0,5,2)



distance_table=get_distance_table(g,0)
print(distance_table)


dijsktra(g,0,5)

