"""
File: algorithm.py
Graph-processing algorithms
"""
from linkedstack import LinkedStack
from minheap import MinHeap

def topoSort(g, startLabel = None):
    """
    Input:
        A DAG object (LinkedDirectedGraph)
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
    
    # mark all vertices as unvisited
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
            
def repairQueue(g, startLabel = None):
    """
    Input:
        A graph object (LinkedDirectedGraph)
    Output:
        A list of undirected edges (list)
        e.g, [(1, ("A", "B")), (2, ("B", "C")), (3, ("C", "D"))]
        
    The function returns all unique undirected edges in the graph, sorted by weight.
    
    """
    # mark all edges as unvisited
    visited_edges = set()
    
    # min-heap priority queue
    pq = MinHeap()
    
    # Add each edge into the min-heap priority queue
    for edge in g.edges():
        
        from_v = edge.getFromVertex()
        to_v = edge.getToVertex()
        key = tuple(sorted((from_v.getLabel(), to_v.getLabel()))) # works for undirected edged to avoid duplicate addition
        
        if key not in visited_edges:
            pq.add((edge.getWeight(),key))
            visited_edges.add(key)
    
    # Pop the items from priority queue and add them to list
    result = []
    while not pq.isEmpty():
        edge = pq.pop()
        result.append(edge)
    
    return result
    

def shortestPaths(g, startLabel):
    """
    Input:
        A graph object and the start vertex (LinkedDirectedGraph, string)
    Output:
        A dictionary mapping each reachable vertex to:
        {
        "edge": LinkedEdge used tp reach it
        "cost": total distance from start vertex
        }

    This function using Dijkstra's algorithm to find the shortest paths from a given start vertex on the graph.
    """

    distances = {v.getLabel(): float("inf") for v in g.getVertices()}
    distances[startLabel] = 0

    predecessors = {}

    visited = set()

    heap = MinHeap()
    heap.add((0, startLabel))

    while not heap.isEmpty():
        current_dist, current_label = heap.pop()

        if current_label in visited:
            continue
        visited.add(current_label)

        for edge in g.incidentEdges(current_label):
            neighbor = edge.getToVertex().getLabel()
            weight = edge.getWeight()
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = edge
                heap.add((new_dist, neighbor))

    return {
        label: {
            "edge": edge,
            "cost": distances[neighbor]
        }
        for label, edge in predecessors.items()
    }