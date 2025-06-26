"""
Yao Xu
06/27/2025

In this program, we implemented three methods: getMazeFromFile(), findStartPos() and getOut().
"""

def main():
    maze = getMazeFromFile()
    print(maze)
    # (startRow, startCol) = findStartPos(maze)
    # success = getOut(startRow, startCol, maze)
    # if success:
    #     print("Maze solved:")
    #     print(maze)
    # else:
    #     print("No path out of this maze")
    
def getMazeFromFile():
    with open("maze.txt") as f:
        maze = f.readlines().rstrip('\n')
        print(type(maze))
        return maze

# def findStartPos(maze):
#
# def getOut(row, column, maze):

if __name__ == "__main__": 
    main()