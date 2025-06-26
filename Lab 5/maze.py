"""
Yao Xu
06/27/2025

In this program, we implemented three methods: getMazeFromFile(), findStartPos() and getOut().
"""
from grid import Grid


def main():
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)
    # success = getOut(startRow, startCol, maze)
    # if success:
    #     print("Maze solved:")
    #     print(maze)
    # else:
    #     print("No path out of this maze")
    
def getMazeFromFile():
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
    for row in range (maze.getHeight()):
        for col in range(maze.getWidth()):
            if maze[row][col] == 'P':
                print(row)
                print(col)
                return (row, col)

# def getOut(row, column, maze):

if __name__ == "__main__": 
    main()