import ipdb
class Vertex:
    def __init__(self, id):
        self.id = id 
        self.connectedTo = {}
        
    def addNeighbor(self, v, w=0):
        self.connectedTo[v] = w 
        
    def __str__(self):
        return str(self.id) + " connectedTo " + str([x.id for x in self.connectedTo.keys()])
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getId(self):
        return self.id 
        
    def getWeight(self, v):
        return self.connectedTo[v]       

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVert = 0 
        
    def addVert(self, id):
        self.numVert += 1
        newVertex = Vertex(id)
        self.vertList[id] = newVertex
        return newVertex
        
    def getVertex(self, id):
        if id not in self.vertList:
            return None 
        return self.vertList[id]
        
    def addEdge(self, f, t, w=0):
        if f not in self.vertList:
            f = self.addVert(f)
        if t not in self.vertList:
            t = self.addVert(t)
            
        self.vertList[f].addNeighbor(self.vertList[t], w)
        
    def getVertices(self):
        return self.vertList.keys()
        
    def __iter__(self):
        return iter(self.vertList.values())
        
g = Graph()
for i in range(6):
    g.addVert(i)
    
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for f in g:
    for t in f.getConnections():
        print("(%s, %s)" % (f.getId(), t.getId()))
    
from collections import deque    
def BFS(startVertex, id):
    queue = deque([startVertex])
    visitedVertices = set()
    while len(queue) > 0:
        vertex = queue.pop()
        if vertex in visitedVertices:
            continue 
        if vertex.id == id:
            return True 
        visitedVertices.add(vertex)    
        for v1 in vertex.getConnections():
            if v1 not in visitedVertices:
                queue.appendleft(v1)
    return False 

for i in range(10):    
    print(BFS(g.vertList[0], i))    