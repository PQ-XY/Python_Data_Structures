"""
File: testdirected.py

Defines and tests the all pairs shortest paths algorithm of Floyd.
"""

from graph import LinkedDirectedGraph
import random
from arrays import Array

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

# Define a function that uses Floyd's algorithm
def allPairsShortestPaths(matrix):
    # your code here

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

# Create a randomly ordered list of labels
lyst = list("ABCDEFG")
random.shuffle(lyst)

# Create a graph with those vertex labels
graph = LinkedDirectedGraph(lyst)

# Create the label table for the graph
table = graph.makeLabelTable()
keys = list(table.keys())
keys.sort()

# Add some edges with weights and print the graph
for i in range(len(keys) - 1):
    graph.addEdge(keys[i], keys[i + 1], i)
print("\nThe graph:")
print(graph)

# Create and print the labeled distance matrix
matrix = graph.makeDistanceMatrix(table)
print("\nThe initial labeled distance matrix:")
printDistanceMatrix(matrix, table)

# Run Floyd's algorithm on the distance matrix
allPairsShortestPaths(matrix)

# Print the labeled matrix again
print("\nThe labeled distance matrix will all pairs shortest paths:")
printDistanceMatrix(matrix, table)
