"""
File: model.py
The model for testing graph-processing algorithms.

The programs modify the run() method to perform input validation for the grpah
before running the algorithm on it.
"""

from graph import LinkedDirectedGraph

class GraphDemoModel(object):
    """The model class for the application."""
    
    def __init__(self):
        self.graph = None
        self.startLabel = None

    def createGraph(self, rep, startLabel):
        """Creates a graph from rep and startLabel.
        Returns a message if the graph was successfully
        created or an error message otherwise."""
        self.graph = LinkedDirectedGraph()
        self.startLabel = startLabel
        edgeList = rep.split()

        for edge in edgeList:
            if '>' not in edge:
                # A disconnected vertex
                if not self.graph.containsVertex(edge):
                    self.graph.addVertex(edge)
                else:
                    self.graph = None
                    return "Duplicate vertex"
            else:
                # Two vertices and an edge
                bracketPos = edge.find('>')
                colonPos = edge.find(';')
                if bracketPos == -1 or colonPos == -1 or bracketPos > colonPos:
                    self.graph = None
                    return "Problem with > or ;"
                
                fromLabel = edge[:bracketPos]
                toLabel = edge[bracketPos + 1:colonPos]
                weight = edge[colonPos + 1:]

                if weight.isdigit():
                    weight = int(weight)

                if not self.graph.containsVertex(fromLabel):
                    self.graph.addVertex(fromLabel)
                if not self.graph.containsVertex(toLabel):
                    self.graph.addVertex(toLabel)
                if self.graph.containsEdge(fromLabel, toLabel):
                    self.graph = None
                    return "Duplicate edge"

                self.graph.addEdge(fromLabel, toLabel, weight)

        vertex = self.graph.getVertex(startLabel)
        if vertex is None:
            self.graph = None
            return "Start label not in graph"
        else:
            vertex.setMark()
            return "Graph created"

    def getGraph(self):
        """Returns the string rep of the graph or None if it is unavailable"""
        if not self.graph:
            return None
        else:
            return str(self.graph)

    def run(self, algorithm):
        """
        Runs the given algorithm on the graph and returns its result,
        or None if the graph is unavailable.
        
        Parameters:
            algorithm: a function like topoSort, dijkstra, or spanTree
        
        Returns:
            result of algorithm(graph, startLabel), or raises ValueError if graph is invalid.
        """
        if self.graph is None:
            return None
        
        # Input validation for the graph
        if algorithm.__name__  == "topoSort": # must be a DAG
            if not self.graph.isDirected() or self.graph.hasCycle():
                raise ValueError("Invalid graph! The graph must be a DAG")
        elif algorithm.__name__  == "spanTree": # must be undirected connected graph and are weighted
            if not self.graph.isConnected(self.startLabel) or self.graph.isDirected():
                raise ValueError("Invalid graph! The graph must be undirected connected")
        return algorithm(self.graph, self.startLabel)
        
if __name__ == "__main__":
    testModel = GraphDemoModel()
    testModel.createGraph("A B C A>B;5 B>A;5 B>C;7 C>B;7 A>C;7 C>A;7","B")
    
    theGraph = testModel.getGraph()
    print("\nThe graph:")
    print(theGraph)
    
    print("\nincidentEdges of A (outgoing)")
    edgeAB = testModel.graph.incidentEdges("A")
    for i in edgeAB:
        print(i)
        
    print("\nAll vertices:")
    for i in testModel.graph.getVertices():
        print(i)
    
    print("\nAll edges:")
    for i in testModel.graph.edges():
        print(i)
    
    print("\nnubmer of vertices:")
    print(len(list(testModel.graph.getVertices())))

    print("\nVertex B's neighbors:")
    for i in testModel.graph.neighboringVertices("B"):
        print(i)
        
    print("\nVertex B's edge list:")
    vertexB = testModel.graph.vertices["B"]
    vertexBNeighbors = vertexB.neighboringVertices()
    for i in vertexB.edgeList:
        print(i)
    
    print("\nVertex A's edge list:")
    vertexA = testModel.graph.vertices["A"]
    for i in vertexA.edgeList:
        print(i)
        
    print("\nIs the graph connected?")
    print(testModel.graph.isConnected("A"))
    
    print("\nIs the graph directed?")
    print(testModel.graph.isDirected())
    
    print("\nDoes the grpah have cycles?")
    print(testModel.graph.hasCycle())