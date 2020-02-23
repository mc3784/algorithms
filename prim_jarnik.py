import heapq
from graph import Graph


class PriorityEntry(object):

    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


def prim_jarnik(graph,start_v):
	visited=[]
	q=[]
	heapq.heappush(q,PriorityEntry(0,start_v))
	spanning_cost=0
	while len(visited)<graph.numVertex:
		current=heapq.heappop(q)
		current_vertex=current.data
		current_distance=current.priority
		visited.append(current_vertex)
		print(current_distance)
		spanning_cost+=current_distance
		for v in graph.get_adjacency_list(current_vertex):
			if v not in visited:
				edge_weight=graph.adjacencyMatrix[current_vertex][v]
				heapq.heappush(q,PriorityEntry(edge_weight,v))
	print(visited)
	print(spanning_cost)



g=Graph(8)

g.add_edge(0,1,1)
g.add_edge(1,2,2)

g.add_edge(1,3,6)
g.add_edge(2,3,2)
g.add_edge(1,4,3)
g.add_edge(3,5,1)
g.add_edge(5,4,5)
g.add_edge(3,6,1)
g.add_edge(6,7,1)
g.add_edge(0,7,8)


prim_jarnik(g,0)
