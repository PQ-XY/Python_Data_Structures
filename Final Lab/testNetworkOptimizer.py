"""
Test Driver for Smart City Utility Network Optimizer
"""

from model import GraphDemoModel
from algorithm import spanTree, repairQueue, shortestPaths

def display_repair_queue(queue):
    for item in queue:
        print(f"Urgency {item[0]}: {item[1][0].getLabel()} <-> {item[1][1].getLabel()}")

def case_1_mst():
    print("===== Case 1: Minimum Spanning Tree (Optimized Layout) =====")
    model = GraphDemoModel()
    
    # Sample undirected weighted graph representation (MST requires undirected and connected graph)
    # Assume: A-B (5), B-C (4), A-C (6), C-D (3)
    graph_input = "A>B;5 B>A;5 B>C;4 C>B;4 A>C;6 C>A;6 C>D;3 D>C;3"
    start_vertex = "A"
    
    msg = model.createGraph(graph_input, start_vertex)
    print("Graph creation:", msg)
    print("Original Graph:\n", model.getGraph())

    try:
        mst_edges = model.run(spanTree)
        print("\nMST Result (undirected edges):")
        for edge in mst_edges:
            print(edge)
        
    except ValueError as e:
        print("MST Error:", e)

def case_2_repair_queue():
    print("\n===== Case 2: Repair Priority Queue =====")
    model = GraphDemoModel()

    # Same graph as above can be reused (assume each edge represents a repair need with urgency = weight)
    graph_input = "A>B;1 B>A;1 B>C;2 C>B;2 A>C;3 C>A;3 C>D;4 D>C;4"
    start_vertex = "A"

    msg = model.createGraph(graph_input, start_vertex)
    print("Graph creation:", msg)
    print("Original Graph:\n", model.getGraph())

    repair_tasks = model.run(repairQueue)
    print("\nRepair Queue (by urgency):")
    for urgency, (v1, v2) in repair_tasks:
        print(f"Urgency {urgency}: {v1} <-> {v2}")

def case_3_shortest_paths():
    print("\n===== Case 3: Shortest Paths =====")
    model = GraphDemoModel()

    # assume each edge weight represents the distance from one vertice to another
    graph_input = "A>B;2 B>A;2 A>D;7 D>A;7 B>C;3 C>B;3 B>D;4 D>B;4 C>F;1 F>C;1 D>E;2 E>D;2 D>F;1 F>D;1 E>F;5 F>E;5"
    start_vertex = "A"

    msg = model.createGraph(graph_input, start_vertex)
    print("Graph creation:", msg)
    print("Original Graph:\n", model.getGraph())

    result = model.run(shortestPaths)

    for vertex, info in result.items():
        print(f"To {vertex}: via {info['edge']}, cost = {info['cost']}")


if __name__ == "__main__":
    case_1_mst()
    case_2_repair_queue()
    case_3_shortest_paths()