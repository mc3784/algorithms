import numpy as np

class Graph():
    
    def __init__(self,numVertex,isDirected=False):
        self.isDirected=isDirected
        self.numVertex=numVertex
        self.adjacencyMatrix=np.zeros((self.numVertex,self.numVertex))

    def add_edge(self,v1,v2,w=1):
        self.adjacencyMatrix[v1][v2]=w
        if not self.isDirected:
            self.adjacencyMatrix[v2][v1]=w

    def get_adjacency_list(self,v):
        adjacency_list=[]
        for i in range(self.numVertex):
            if self.adjacencyMatrix[v][i]!=0:
                adjacency_list.append(i)
        return adjacency_list

    def get_indegree(self,v):
        in_degree=0
        for i in range(self.numVertex):
            if self.adjacencyMatrix[i][v]==1:
                in_degree+=1
        return in_degree

    def display(self):
        for i in range(self.numVertex):
            for j in range(self.numVertex):
                if self.adjacencyMatrix[i][j]==1:
                    print(str(i)+"-->" +str(j))



#g=Graph(4)
#g.add_edge(0,1)
#g.add_edge(0,2)
#g.add_edge(1,3)

#g.display()

