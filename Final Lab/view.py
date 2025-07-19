"""
File: view.py
The view for testing graph-processing algorithms.
"""
from model import GraphDemoModel
from algorithm import shortestPaths, spanTree, topoSort

class GraphDemoView(object):
    """The view class for the application"""

    def __init__(self):
        self.model = GraphDemoModel()

    def run(self):
        """Menu-driven command loop for the app."""
        menu = "Main menu\n" + \
               " 1 Input a graph from the keyboard\n" + \
               " 2 Input a graph from a file\n" + \
               " 3 View the current graph\n" \
               " 4 Single-source shortest paths\n" \
               " 5 Minimum spanning tree\n" \
               " 6 Exit the program\n"
        while True:
            command = self.getCommand(6, menu)
            if command == 1:
                self.getFromKeyboard()
            elif command == 2:
                self.getFromFile()
            elif command == 3:
                print(self.model.getGraph())
            elif command == 4:
                print("Paths:\n",
                  self.model.run(shortestPaths))
            elif command == 5:
                print("Tree:",
                    " ".join(map(str,
                            self.model.run(spanTree))))
            else:
                break

    def getCommand(self, high, menu):
        """Obtains and returns a command number."""
        while True:
            try:
                print(menu)
                cmd = int(input("Enter a command: "))
                if 1 <= cmd <= high:
                    return cmd
                else:
                    print("Please enter a number between 1 and", high)
            except ValueError:
                print("Invalid input. Please enter a number.")


    def getFromKeyboard(self):
        """Inputs a description of the graph from the
        keyboard and creates the graph."""
        rep = ""
        while True:
            edge = input("Enter an edge or return to quit: ")
            if edge == "": break
            rep += edge + " "
        startLabel = input("Enter the start label: ")
        print(self.model.createGraph(rep, startLabel))

    def getFromFile(self):
        """Inputs a description of the graph from a file
        and creates the graph."""
        filename = input("Enter a filename: ")
        try:
            with open(filename, "r") as file:
                rep = file.readline().strip()
                startLabel = file.readline().strip()
                print(self.model.createGraph(rep, startLabel))
        except FileNotFoundError:
            print("File not found.")