"""
File: graph.py

The program adds three methods in Class LinkedDirectedGraph():
    isDirected() : Return True if the graph is directed or False otherwise.
    hasCycle() : Return True if the graph has cycle or False otherwise. 
    isConnected() : Return True if the graph is connected or False otherwise.
    
Other added methods:
    LinkedEdge(): 
        getFromVertex() : Returns the edge's start vertex.
        __lt__ : Supports comparison edges by weight
    
        
"""

from abstractcollection import AbstractCollection
from grid import Grid

class LinkedEdge(object):
    
    # An edge has a source vertex, a destination vertex,
    # a weight, and a mark attribute.

    def __init__(self, fromVertex, toVertex, weight = None):         
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight 
        self.mark = False
    
    def clearMark(self):
        """Clears the mark on the edge."""
        self.mark = False
    
    def __eq__(self, other):
        """Two edges are equal if they connect
        the same vertices."""
        if self is other: return True
        if type(self) != type(other):
            return False
        return self.vertex1 == other.vertex1 and \
               self.vertex2 == other.vertex2
    
    def getOtherVertex(self,  thisVertex):
        """Returns the vertex opposite thisVertex."""
        if thisVertex == None or thisVertex == self.vertex2:
            return self.vertex1
        else:
            return self.vertex2

    def getToVertex(self):
        """Returns the edge's destination vertex."""
        return self.vertex2
    
    def getFromVertex(self):
        """Returns the edge's start vertex."""
        return self.vertex1
    
    def getWeight(self):
        """Returns the edge's weight."""
        return self.weight
    
    def isMarked(self): 
        """Returns True if the edge is marked
        or False otherwise."""
        return self.mark
    
    def setMark(self):
        """Sets the mark on the edge."""
        self.mark = True
    
    def setWeight(self, weight):
        """Sets the weight on the edge to weight."""
        self.weight = weight     
          
    def __lt__(self, other):
        return self.getWeight() < other.getWeight()

    def __str__(self):
        """Returns the string representation of the edge."""
        return str(self.vertex1) + ">" + \
               str(self.vertex2)   + ":" + \
               str(self.weight)

class LinkedVertex(object):

    # A vertex has a label, a list of incident edges,
    # and a mark attribute.

    def __init__(self, label):
        self.label = label
        self.edgeList = list()
        self.mark = False

    def clearMark(self):
        """Clears the mark on the vertex."""
        self.mark = False;
    
    def getLabel(self): 
        """Returns the label of the vertex."""
        return self.label
    
    def isMarked(self): 
        """Returns True if the vertex is marked
        or False otherwise."""
        return self.mark
    
    def setLabel(self, label, g):
        """Sets the vertex's label to label."""
        g.vertices.pop(self.label, None)
        g.vertices[label] = self
        self.label = label          

    def setMark(self):
        """Sets the mark on the vertex."""
        self.mark = True
    
    def __str__(self):
        """Returns the string representation of the vertex."""
        return str(self.label)

    def __eq__(self, other):
        """Two vertices are equal if they have
        the same labels."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.getLabel() == other.getLabel()

    def __hash__(self):
        """Supports hashing on a vertex."""
        return hash(self.label)

    # Methods used by LinkedGraph
    
    def addEdgeTo(self, toVertex, weight):
        """Connects the vertices with an edge."""
        edge = LinkedEdge(self, toVertex, weight)
        self.edgeList.append(edge)
    
    def getEdgeTo(self, toVertex):
        """Returns the connecting edge if it exists, or
        None otherwise."""
        edge = LinkedEdge(self, toVertex)
        try:
            return self.edgeList[self.edgeList.index(edge)]
        except:
            return None

    def incidentEdges(self):
        """Returns the incident edges of this vertex."""
        return iter(self.edgeList)
        
    def neighboringVertices(self):
        """Returns the neighboring vertices of this vertex."""
        vertices = list()
        for edge in self.edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)
            
    def removeEdgeTo(self, toVertex):
        """Returns True if the edge exists and is removed,
        or False otherwise."""
        edge = LinkedEdge(self, toVertex)
        if edge in self.edgeList:
            self.edgeList.remove(edge)
            return True
        else:
            return False


class LinkedDirectedGraph(AbstractCollection):

    INFINITY = "-"   # For building a distance matrix

    # A graph has a count of vertices, a count of edges,
    # and a dictionary of label/vertex pairs.

    def __init__(self, sourceCollection = None):
        self.edgeCount = 0
        self.vertices = {}
        AbstractCollection.__init__(self, sourceCollection)
        
    # Methods for clearing, marks, sizes, string rep

    def clear(self):
        """Clears the graph."""
        self.size = 0
        self.edgeCount = 0
        self.vertices = {}        

    def clearEdgeMarks(self):
        """Clears all the edge marks."""
        for edge in self.edges():
            edge.clearMark()
    
    def clearVertexMarks(self):
        """Clears all the vertex marks."""
        for vertex in self.getVertices():
            vertex.clearMark()
    
    def sizeEdges(self):
        """Returns the number of edges."""
        return self.edgeCount
    
    def sizeVertices(self):
        """Returns the number of vertices."""
        return len(self)
    
    def __str__(self):
        """Returns the string representation of the graph."""
        result = str(len(self)) + " Vertices: "
        for vertex in self.vertices:
            result += " " + str(vertex)
        result += "\n";
        result += str(self.sizeEdges()) + " Edges: "
        for edge in self.edges():
            result += " " + str(edge)
        return result

    def add(self, label):
        """For compatibility with other collections."""
        self.addVertex(label)

    # Vertex related methods
    
    def addVertex(self, label):
        """Precondition: a vertex with label must not
        already be in the graph.
        Raises: AttibuteError if a vertex with label
        is already in the graph."""
        if self.containsVertex(label):
            raise AttributeError("Label " + str(label) + " already in graph.""")
        self.vertices[label] = LinkedVertex(label)
        self.size += 1
        
    def containsVertex (self, label):
        return label in self.vertices
    
    def getVertex(self, label):
        """Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        if not self.containsVertex(label):
            raise AttributeError("Label " + str(label) + " not in graph.""")
        return self.vertices[label]
    
    def removeVertex(self,  label):
        """Returns True if the vertex was removed, or False otherwise."""
        removedVertex = self.vertices.pop(label, None)
        if removedVertex is None: 
            return False
        
        # Examine all other vertices to remove edges
        # directed at the removed vertex
        for vertex in self.getVertices():
            if vertex.removeEdgeTo(removedVertex): 
                self.edgeCount -= 1

        # Examine all edges from the removed vertex to others
        for edge in removedVertex.incidentEdges():
            self.edgeCount -= 1
        self.size -= 1
        return True
    
    # Methods related to edges

    def addEdge(self, fromLabel, toLabel, weight):
        """Connects the vertices with an edge with the given weight.
        Preconditions: vertices with fromLabel and toLabel must
        already be in the graph.
        The vertices must not already be connected by an edge.
        Raises: AttibuteError if the vertices
        are not already in the graph or they are already connected."""
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)
        if self.getEdge(fromLabel, toLabel):
            raise AttributeError("An edge already connects " + \
                                 str(fromLabel) + " and " + \
                                 str(toLabel))
        fromVertex.addEdgeTo(toVertex, weight)
        self.edgeCount += 1
    
    def containsEdge(self, fromLabel, toLabel):
        """Returns True if an edge connects the vertices,
        or False otherwise."""
        return self.getEdge(fromLabel, toLabel) != None
    
    def getEdge(self, fromLabel, toLabel):
        """Returns the edge connecting the two vertices, or None if
        no edge exists.
        Precondition: vertices with fromLabel and toLabel must
        already be in the graph.
        Raises: AttibuteError if the vertices
        are not already in the graph."""
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)     
        return fromVertex.getEdgeTo(toVertex)
    
    def removeEdge (self, fromLabel, toLabel): 
        """Returns True if the edge was removed, or False otherwise.
        Precondition: vertices with fromLabel and toLabel must
        already be in the graph.
        Raises: AttibuteError if the vertices
        are not already in the graph."""
        fromVertex = self.getVertex(fromLabel)     
        toVertex   = self.getVertex(toLabel)     
        edgeRemovedFlg = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlg: 
            self.edgeCount -= 1
        return edgeRemovedFlg

    # Iterators
    
    def __iter__(self):
        """Supports iteration over a view of self (the vertices)."""
        return self.getVertices()

    def edges(self):
        """Supports iteration over the edges in the graph."""
        result = list()
        for vertex in self.getVertices():
            result += list(vertex.incidentEdges())
        return iter(result)
    
    def getVertices(self):
        """Supports iteration over the vertices in the graph."""
        return iter(self.vertices.values())

    def incidentEdges(self, label):
        """Supports iteration over the incident edges of the
        given verrtex.
        Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        return self.getVertex(label).incidentEdges()
    
    def neighboringVertices(self, label):
        """Supports iteration over the neighboring vertices of the
        given verrtex.
        Precondition: a vertex with label must already be in the graph.
        Raises: AttibuteError if a vertex with label is not already in the graph."""
        return self.getVertex(label).neighboringVertices()
    
    # Make a table of vertex labels and indicies for a matrix
    def makeLabelTable(self):
        """Returns a table (dictionary) associating vetrex labels with
        index positions."""
        labels = list(map(lambda vertex: vertex.getLabel(),
                          self))
        labels.sort()
        table = dict()
        index = 0
        for label in labels:
            table[label] = index
            index += 1
        return table

    def makeDistanceMatrix(self, table):
        """Returns a distance matrix for the given graph and its label table."""
        matrix = Grid(len(self), len(self), LinkedDirectedGraph.INFINITY)
        for vertex in self.getVertices():
            vertexLabel = vertex.getLabel()
            vertexIndex = table[vertexLabel]
            matrix[vertexIndex][vertexIndex] = 0
            for neighbor in self.neighboringVertices(vertexLabel):
                neighborLabel = neighbor.getLabel()
                neighborIndex = table[neighborLabel]
                weight = self.getEdge(vertexLabel, neighborLabel).getWeight()
                matrix[vertexIndex][neighborIndex] = weight
        return matrix
    
    # Method for checking the type of graph

    def isDirected(self):
        """
        Input:
            None
        Output:
            True if the grpah is directed or False otherwise (boolean)
            
        The function returns True if the grpah is directed or False otherwise.
        """
        edge_set = set((edge.getFromVertex(), edge.getToVertex()) for edge in self.edges())
        for from_v, to_v in edge_set:
            if (to_v, from_v) not in edge_set:
                return True
        return False
            
    
    def hasCycle(self):
        """
        Input:
            None
        Output:
            True if the grpah has a cycle or False otherwise (boolean)
            
        The function returns True if the grpah has a cycle or False otherwise.
        Works on undirected graphs with possibly disconnected components.
        
        """
        def dfs_findCycle(graph, label, visited, predecessor):
            """A helper function that performs depth-first search and return False
                if coming across the same vertex and its predecessor is not the
                starting vertex.
            """
            # mark v as visited
            visited.add(label)
            # for each vertex, w, adjacent to v:
            for neighbor in graph.neighboringVertices(label):
                neighbor_label = neighbor.getLabel()
                # if w is unvisited:
                if neighbor_label not in visited:        
                    if dfs_findCycle(graph, neighbor_label, visited, label):
                        return True
                elif neighbor_label in visited and neighbor_label != predecessor:
                    return True
            return False
        
        # The grpah might have disconnected components so to avoid redundant work,
        # visited_vertices should be shared across when looping through each vertex
        visited_vertices = set()
        for vertex in self.getVertices():
            vertex_label = vertex.getLabel()
            # keep track of predecessor to avoid a false positive for a cycle
            preceding_vertex = None
            if vertex_label not in visited_vertices:
                if(dfs_findCycle(self, vertex_label, visited_vertices, preceding_vertex)):
                    return True

        return False
    
    def isConnected(self, start_label):
        """
        Input:
            The label of vertex (string)
        Output:
            True if the grpah is connected or False otherwise (boolean)
            
        The function returns True if the grpah is connected or False otherwise.
        
        """
        def dfs(graph, label, visited):
            """A helper function that performs depth-first search"""
            # mark v as visited
            visited.add(label)
            # for each vertex, w, adjacent to v:
            for neighbor in graph.neighboringVertices(label):
                neighbor_label = neighbor.getLabel()
                # if w is unvisited:
                if neighbor_label not in visited:
                    dfs(graph, neighbor_label, visited)
                    
        visited_vertices = set()
        dfs(self, start_label, visited_vertices)
        
        return len(visited_vertices) == len(list(self.getVertices()))
       
        

