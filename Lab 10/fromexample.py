"""
File: fromexample.py

Defines and tests the all pairs shortest paths algorithm of Floyd.
Uses the graph from Figure 12.19 of the text, as represented in the
file example.txt.
"""

from graph import LinkedDirectedGraph
from arrays import Array
from testdirected import allPairsShortestPaths

# Functions for working with infinity

def isLessWithInfinity(a, b):
    """Returns False if a == b or a == INFINITY and b != INFINITY.
    Otherwise, returns True if b == INFINITY or returns a < b."""
    if a == LinkedDirectedGraph.INFINITY and b == LinkedDirectedGraph.INFINITY:
        return False
    elif b == LinkedDirectedGraph.INFINITY: return True
    elif a == LinkedDirectedGraph.INFINITY: return False
    else: return a < b

def addWithInfinity(a, b):
    """If a == INFINITY or b == INFINITY, returns INFINITY.
    Otherwise, returns a + b."""
    if a == LinkedDirectedGraph.INFINITY or b == LinkedDirectedGraph.INFINITY:
        return LinkedDirectedGraph.INFINITY
    else: return a + b

# Define a function to print a labeled distance matrix
def printDistanceMatrix(matrix, table):
    """Prints the distance matrix with rows and columns
    labels with the index positions and vertex labels."""
    labels = Array(len(table))
    index = 0
    labelWidth = 0
    indexWidth = 0
    for label in table:
        labels[table[label]] = label
        labelWidth = max(labelWidth, len(str(label)))
        indexWidth = max(indexWidth, len(str(index)))
        index += 1

    weightWidth = 0
    for row in range(matrix.getHeight()):
        for column in range(matrix.getWidth()):
            weightWidth = max(weightWidth, len(str(matrix[row][column])))

    weightWidth = max(weightWidth, labelWidth, indexWidth)
    topRowLeftMargin = " " * (indexWidth + labelWidth + 3)
    print(topRowLeftMargin, end = "")
    for label in labels:
        print(centerJustify(label, weightWidth), end = " ")
    print()
    print(topRowLeftMargin, end = "")
    for position in range(len(labels)):
        print(centerJustify(position, weightWidth), end = " ")
    print("\n")
    for row in range(matrix.getHeight()):
        print(rightJustify(row, indexWidth),
              rightJustify(labels[row], labelWidth), end = "  ")
        for column in range(matrix.getWidth()):
            print(centerJustify(matrix[row][column], weightWidth), end = " ")
        print()

def rightJustify(data, fieldWidth):
    """Right-justifies data within the given field width."""
    data = str(data)
    numSpaces = fieldWidth - len(data)
    if numSpaces <= 0:
        return data
    else:
        return " " * numSpaces + data

def centerJustify(data, fieldWidth):
    """Centers data within the given field width."""
    data = str(data)
    numSpaces = fieldWidth - len(data)
    if numSpaces <= 0:
        return data
    else:
        spacesLeft = numSpaces // 2
        spacesRight = numSpaces // 2
        if numSpaces % 2 == 1:
            spacesLeft += 1
    return spacesLeft * " " + data + spacesRight * " "

def createGraphFromFile():
    """Creates a graph from a file.
    Returns the graph if it was successfully
    created or an error message otherwise."""
    fileName = input("Enter the file name: ")
    theFile = open(fileName, 'r')
    graph = LinkedDirectedGraph()
    rep = theFile.read()
    edgeList = rep.split()
    for edge in edgeList:
        if not '>' in edge:
            # A disconnected vertex
            if not graph.containsVertex(edge):
                graph.addVertex(edge)
            else:
                graph = None
                return "Duplicate vertex"
        else:
            # Two vertices and an edge
            bracketPos = edge.find('>')
            colonPos = edge.find(':')
            if bracketPos == -1 or colonPos == -1 or \
               bracketPos > colonPos:
                graph = None
                return "Problem with > or :"
            fromLabel = edge[:bracketPos]
            toLabel = edge[bracketPos + 1:colonPos]
            weight = edge[colonPos + 1:]
            if weight.isdigit():
                weight = int(weight)
            if not graph.containsVertex(fromLabel):
                graph.addVertex(fromLabel)
            if not graph.containsVertex(toLabel):
                graph.addVertex(toLabel)
            if graph.containsEdge(fromLabel, toLabel):
                graph = None
                return "Duplicate edge"
            graph.addEdge(fromLabel, toLabel, weight)
    return graph

# Get a graph from a file
graph = createGraphFromFile()
if type(graph) == str:
    print(graph)
else:
    # Create the label table for the graph
    table = graph.makeLabelTable()

    # Create and print the labeled distance matrix
    matrix = graph.makeDistanceMatrix(table)
    print("\nThe initial labeled distance matrix:")
    printDistanceMatrix(matrix, table)

    # Run Floyd's algorithm on the distance matrix
    allPairsShortestPaths(matrix)

    # Print the labeled matrix again
    print("\nThe labeled distance matrix will all pairs shortest paths:")
    printDistanceMatrix(matrix, table)
