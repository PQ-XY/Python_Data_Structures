"""
File: algorithm.py
Graph-processing algorithms
"""
from linkedstack import LinkedStack

def topoSort(g, startLabel = None):
    """
    Input:
        A DAG object and the start vertex (LinkedDirectedGraph, string)
    Output:
        The topological order of the vertices
        
    The function returns the topological order of the vertices
    
    """
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.getVertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    """
    A helper function : Depth-first search
    """
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)

def spanTree(g, startLabel):
    """
    Input:
        A graph object and the start vertex (LinkedDirectedGraph, string)
    Output:
        A list of edges (list)
        
    The function returns the list of edges that connects all vertices with minimum total weight.
    Works on undirected connected graph.
    
    """
    
    # mark all edges as unvisited
    visited_vertices = set()
    
    # mark some vertex, say v, as visited
    start_vertex = g.getVertex(startLabel)
    visited_vertices.add(start_vertex)
    
    # Instantiate a min-heap priority queue
    pq = MinHeap()
    
    # for each edge leading from v:
    for leading_edge in start_vertex.incidentEdges():
        # add the edge to the min-heap priority queue
        pq.add(leading_edge)
        
    # MST edges
    result = []
    
    # while k < number of vertices:
    while len(visited_vertices) < g.sizeVertices() and not pq.isEmpty():
        # pop an edge from the heap
        minWeight_edge = pq.pop()
        # the other end of the edge
        from_v = minWeight_edge.getFromVertex()
        to_v = minWeight_edge.getToVertex()
        
        # Determine which vertex is the new one
        if from_v in visited_vertices and to_v not in visited_vertices:
            new_vertex = to_v
        elif to_v in visited_vertices and from_v not in visited_vertices:
            new_vertex = from_v
        else:
            continue  # skip if both ends are visited or both unvisited
            
        visited_vertices.add(new_vertex)
        result.append(minWeight_edge)
        
        # Add new edges from this vertex
        for leading_edge in new_vertex.incidentEdges():
            other = leading_edge.getOtherVertex(new_vertex)
            if other not in visited_vertices:
                pq.add(leading_edge)
    return result
            
def shortestPaths(g, startLabel):
    pass