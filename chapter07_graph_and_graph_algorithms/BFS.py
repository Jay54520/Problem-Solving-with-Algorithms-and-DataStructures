import ipdb
class Vertex:
    def __init__(self, id):
        self.id = id 
        self.connectedTo = {}
        
    def addNeighbor(self, v, w=0):
        self.connectedTo[v] = w
        
    def __str__(self):
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connectedTo])
        
    def getConnections(self):                                                                         
        return self.connectedTo.keys()
        
    def getId(self):
        return self.id 
        
    def getWeight(self, v):
        return self.connectedTo[v]
        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        
    def addVertex(self, id):        
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertList[id] = newVertex
        return newVertex
        
    def getVertex(self, id):
        if id not in self.vertList:
            return None 
        return self.vertList[id]
        
    def __contains__(self, id):
        return id in self.vertList
        
    def addEdge(self, f, t, w=0):
        if f not in self.vertList:
            f = self.addVertex(f)
        if t not in self.vertList:
            t = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], w)
        
    def getVertices(self):
        return self.vertList.keys()
        
    def __iter__(self):
        return iter(self.vertList.values())
        
from collections import deque 
def BST(startVertex, id):
    queue = deque([startVertex])
    visitedVertics = set()
    while len(queue) > 0:
        vertex = queue.pop()
        if vertex in visitedVertics:
            continue
            
        if vertex.id == id:
            return True             
        visitedVertics.add(vertex)
        
        for n in vertex.getConnections():
            if n not in visitedVertics:
                queue.appendleft(n)
                
    return False 
    
g = Graph()    
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,0)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
for v in g.vertList.values():
    for v2 in v.getConnections():
        print("(%s, %s)" % (v.getId(), v2.getId()))
    
print(BST(g.vertList[3], 5))
print(BST(g.vertList[3], 10))

        