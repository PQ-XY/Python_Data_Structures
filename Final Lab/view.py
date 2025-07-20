"""
File: view.py
The view for testing graph-processing algorithms.
"""
from model import GraphDemoModel
from algorithm import shortestPaths, spanTree, topoSort, repairQueue

class GraphDemoView(object):
    """The view class for the application"""

    def __init__(self):
        self.model = GraphDemoModel()

    def run(self):
        """Menu-driven command loop for the app."""
        menu = "\nMain menu\n" + \
               " 1 Input a smart city utility network from the keyboard\n" + \
               " 2 Input a smart city utility network from a file\n" + \
               " 3 View the current smart city utility network\n" \
               " 4 Find shortest paths from start point\n" \
               " 5 Build the most cost-effective utility layout\n" \
               " 6 Generate repair priority list\n" \
               " 7 Exit the program\n"
        while True:
            command = self.getCommand(7, menu)
            if command == 1:
                self.getFromKeyboard()
            elif command == 2:
                self.getFromFile()
                print("-"*50)
            elif command == 3:
                print("Current Network:\n", self.model.getGraph())
                print("-"*50)
            elif command == 4:
                result = self.model.run(shortestPaths)
                print("\nShortest Paths from the start vertex:")
                for vertex, info in result.items():
                    print(f"To {vertex}: via {info['edge']}, cost = {info['cost']}")
                print("-"*50)
            elif command == 5:
              print("\nMost cost-effective utility network(undirected MST):")
              for edge in self.model.run(spanTree):
                  print(edge)
              print("-"*50)
            elif command == 6:
                print("\nRepair Priority:")
                for urgency, (v1, v2) in self.model.run(repairQueue):
                    print(f"Urgency {urgency}: {v1} <-> {v2}")
                print("-"*50)
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

if __name__ == "__main__":
    app = GraphDemoView()
    app.run()