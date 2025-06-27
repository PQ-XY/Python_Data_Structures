"""
Yao Xu
06/27/2025

In this program, we implemented three methods: getMazeFromFile(), findStartPos() and getOut(). In method getMazeFromFile()
we take a text file and transform it into a grid object. In method findStartPos(), we take the grid object as input and
return the starting point. In method getOut(), we take the starting point and the grid object and check if there is a valid
path to the end point 'T'.

I changed the order of the neighbor points that we put in the stack waiting for future check. I found that the paths(marked
as '.') are different. I think because stack is the LIFO, if we change the push order, it changes which direction is explored
first.
"""

from grid import Grid
from linkedstack import LinkedStack

def main():
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)
    success = getOut(startRow, startCol, maze)
    if success:
        print("Maze solved:")
        print(maze)
    else:
        print("No path out of this maze")
    
def getMazeFromFile():
    """
    Returns the maze grid from the txt file
    Input:
        A text file
    Output:
        A maze from the txt file
    """
    with open("maze.txt") as f:
        maze = [line.rstrip('\n') for line in f]
        grid_width = len(maze[0])
        grid_height = len(maze)
        grid = Grid(grid_height, grid_width)

        for row in range(grid_height):
            for col in range(grid_width):
                grid[row][col] = maze[row][col]
        return grid

def findStartPos(maze):
    """
    Find the start position of a maze by going through all the cells.
    Input:
        maze - The maze to be solved.
    Output:
        startRow, startCol - The row and column of the start position.
    """
    for row in range (maze.getHeight()):
        for col in range(maze.getWidth()):
            if maze[row][col] == 'P':
                return (row, col)

def getOut(row, column, maze):
    """
    We try to find a valid path from 'P' to 'T' in the grid.
    Input:
        starting point (row, column), grid that represents the maze
    Output:
        True if maze solved, False otherwise
    """
    rows = maze.getHeight()
    cols = maze.getWidth()
    linked_stack = LinkedStack()
    linked_stack.push((row, column))

    while not linked_stack.isEmpty():
        row, col = linked_stack.pop()

        if not (0 <= row < rows) or not (0 <= col < cols):
            continue
        current = maze[row][col]

        if current =='*' or current == '.':
            continue

        if current == 'T':
            return True

        if current != 'P':
            maze[row][col] = '.'

        neighbors = [(row, col - 1), (row + 1, col), (row, col + 1), (row - 1, col)]

        for r, c in neighbors:
            if 0 <= r < rows and 0 <= c < cols:
                if maze[r][c] == ' ' or maze[r][c] == 'T':
                    linked_stack.push((r, c))
    return False


if __name__ == "__main__": 
    main()