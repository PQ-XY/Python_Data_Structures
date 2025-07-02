"""
Yao Xu
07/02/2025

In this program, we implemented three methods: getMazeFromFile(), findStartPos() and getOut(). In method getMazeFromFile()
we take a text file and transform it into a grid object. In method findStartPos(), we take the grid object as input and
return the starting point. In method getOut(), we take the starting point and the grid object and check if there is a valid
path to the end point 'T'. We also pass a boolean flag to the method to determined whether to use a stack or a queue.

After comparing the test results between the stack version and queue version, I found that we actually explored all the
empty cells before getting to the 'T' point in the queue version, but we skipped some branches with the stack version. So
in this case, the stack version is more efficient in finding out the 'T'. The main difference is that the stack, we go deep
into one path and then come back and go to another. The queue version, we always start step by step from the starting point
and explore all the branches . So if the end point is closer to the starting point, we maybe find it quicker in queue version.
On the other hand, if we have multiple 'T' in the maze, the queue version is more efficient in finding out the closest one.
The stack version may find a 'T', but it could be the closest or any other further 'T'.
"""
import copy

from grid import Grid
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack
from counter import Counter

def main():
    """
    In the main function, I make two copies of the maze for the two tests -- one using stack and another using queue.
    """
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)

    #make deep copies
    maze_stack = copy.deepcopy(maze)
    maze_queue = copy.deepcopy(maze)

    #test stack version
    success_stack = getOut(startRow, startCol, maze_stack, stack_flag=True)
    if success_stack:
        print("Maze solved:")
        print(maze_stack)
    else:
        print("No path out of this maze")

    #test queue version
    success_queue = getOut(startRow, startCol, maze_queue, stack_flag=False)
    if success_queue:
        print("Maze solved:")
        print(maze_queue)
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

def getOut(row, column, maze, stack_flag):
    """
    We try to find a valid path from 'P' to 'T' in the grid.
    Input:
        starting point (row, column), grid that represents the maze, a boolean flag to switch between stack and queue.
    Output:
        True if maze solved, False otherwise
    """
    rows = maze.getHeight()
    cols = maze.getWidth()
    counter = Counter()

    if stack_flag:
        data_structure = LinkedStack()
        add = data_structure.push
        remove = data_structure.pop
    else:
        data_structure = LinkedQueue()
        add = data_structure.add
        remove = data_structure.pop

    add((row, column))
    counter.increment(1)

    while not data_structure.isEmpty():
        row, col = remove()

        if not (0 <= row < rows) or not (0 <= col < cols):
            continue
        current = maze[row][col]

        if current =='*' or current == '.':
            continue

        if current == 'T':
            print(f'Total number of choice points required: {counter}')
            return True

        if current != 'P':
            maze[row][col] = '.'

        neighbors = [(row, col + 1), (row - 1, col), (row, col - 1), (row + 1, col)]

        for r, c in neighbors:
            if 0 <= r < rows and 0 <= c < cols:
                if maze[r][c] == ' ' or maze[r][c] == 'T':
                    add((r, c))
                    counter.increment(1)
    return False


if __name__ == "__main__": 
    main()