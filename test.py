from dijkstra import *
from tools import *

edges = {
    "A": {
        "dst": ["B"],
        "weight": [20],
        "hazard": [1],
        "location": (20, 170, 0)
    },
    "C": {
        "dst": ["D"],
        "weight": [20],
        "hazard": [1],
        "location": (50, 170, 0)
    },
    "F": {
        "dst": ["G"],
        "weight": [20],
        "hazard": [1],
        "location": (80, 170, 0)
    },
    "I": {
        "dst": ["J"],
        "weight": [20],
        "hazard": [1],
        "location": (110, 170, 0)
    },
    "W": {
        "dst": ["V"],
        "weight": [20],
        "hazard": [1],
        "location": (170, 170, 0)
    },
    "B": {
        "dst": ["A", "E"],
        "weight": [20, 36],
        "hazard": [1, 1],
        "location": (20, 140, 0)
    },
    "D": {
        "dst": ["C", "E"],
        "weight": [20, 10],
        "hazard": [1, 1],
        "location": (50, 140, 0)
    },
    "G": {
        "dst": ["F", "H"],
        "weight": [20, 10],
        "hazard": [1, 1],
        "location": (80, 140, 0)
    },
    "J": {
        "dst": ["I", "J"],
        "weight": [20, 10],
        "hazard": [1, 1],
        "location": (110, 140, 0)
    },
    "V": {
        "dst": ["W", "U"],
        "weight": [20, 10],
        "hazard": [1, 1],
        "location": (170, 140, 0)
    },
    "E": {
        "dst": ["B", "D", "H"],
        "weight": [36, 10, 20],
        "hazard": [1, 1, 1],
        "location": (50, 120, 0)
    },
    "H": {
        "dst": ["E", "G", "K"],
        "weight": [20, 10, 20],
        "hazard": [1, 1, 1],
        "location": (80, 120, 0)
    },
    "K": {
        "dst": ["H", "J", "T", "L"],
        "weight": [20, 10, 20, 20],
        "hazard": [1, 1, 1, 1],
        "location": (110, 120, 0)
    },
    "T": {
        "dst": ["K", "U"],
        "weight": [20, 20],
        "hazard": [1, 1],
        "location": (140, 120, 0)
    },
    "U": {
        "dst": ["T", "V"],
        "weight": [20, 10],
        "hazard": [1, 1],
        "location": (170, 120, 0)
    },
    "L": {
        "dst": ["K", "M"],
        "weight": [20, 20],
        "hazard": [1, 1],
        "location": (110, 90, 0)
    },
    "M": {
        "dst": ["L", "N", "P"],
        "weight": [20, 20, 20],
        "hazard": [1, 1, 1],
        "location": (110, 60, 0)
    },
    "P": {
        "dst": ["M", "Q", "S"],
        "weight": [20, 20, 20],
        "hazard": [1, 1, 1],
        "location": (110, 30, 0)
    },
    "S": {
        "dst": ["P"],
        "weight": [20],
        "hazard": [1],
        "location": (110, 0, 0)
    },
    "O": {
        "dst": ["N"],
        "weight": [20],
        "hazard": [1],
        "location": (50, 60, 0)
    },
    "R": {
        "dst": ["Q"],
        "weight": [20],
        "hazard": [1],
        "location": (50, 30, 0)
    },
    "N": {
        "dst": ["O", "M"],
        "weight": [20, 20],
        "hazard": [1, 1],
        "location": (80, 60, 0)
    },
    "Q": {
        "dst": ["R", "P"],
        "weight": [20, 20],
        "hazard": [1, 1],
        "location": (80, 30, 0)
    }

}

exit_array = ["S", "U"]

graph = build_graph(edges)
set_nearest_exit(graph, exit_array)



while(1):
    if input("Print graph? (y/n) ") == ("y" or "Y"):
        draw_graph(graph)
    if input("Print directions? (y/n) ") == ("y" or "Y"):
        for node in graph:
            print("From node:", graph[node].name, "go to:", graph[node].next_node, "and the distance to exit is:",
                  graph[node].distance_to_exit)
    if input("Change hazard intensity? (y/n) ") == ("y" or "Y"):
        a, b = input("Between each nodes? ").split()
        c = int(input("Hazard intensity? "))
        print("changing between", a, "and", b, "to", c)
        change_hazard_intensity(graph[a], graph[b], c, graph, exit_array)

    if input("Do you want to end the program?(y/n) ") == ("y" or "Y"):
        break


