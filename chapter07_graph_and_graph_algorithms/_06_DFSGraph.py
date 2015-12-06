from vertex_graph import Graph, Vertex 

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        
    def dfs(self):
        # Self is an instance of the DFSGraph class 
        for aVertex in self:            
            # Make sure that all nodes in the graph are considered 
            # rather than searching from a chosen starting node 
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
                
    def devisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)