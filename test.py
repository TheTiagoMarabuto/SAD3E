from dijkstra_v2 import *
from tools import*


edges = {
    "A": {
        "dst": ["B", "C", "E"],
        "weight": [12, 13, 15],
        "hazard": [1,1,1],
        "location": (5, 10,0)
    },
    "B": {
        "dst": ["A", "C", "D"],
        "weight": [12, 23, 24],
        "hazard": [1,1,1],
        "location": (10, 10,0)
    },
    "C": {
        "dst": ["A", "B", "D"],
        "weight": [13, 23, 34],
        "hazard": [1,1,1],
        "location": (5, 15,0)
    },
    "D": {
        "dst": ["C", "B"],
        "weight": [34, 24],
        "hazard": [1,1],
        "location": (15, 15,0)
    },
    "E": {
        "dst": ["A", "F"],
        "weight": [15,56],
        "hazard": [1,1],
        "location": (20, 15,0)
    },
    "F": {
        "dst": ["E"],
        "weight": [56],
        "hazard": [1],
        "location": (20, 20,0)
    }

}

exit_array = ["A", "B"]

nodes = build_graph(edges)
set_nearest_exit(nodes, exit_array)

print(nodes["C"].exit, nodes["C"].next_node)

change_hazard_intensity(nodes["C"], nodes["A"], 20)

set_nearest_exit(nodes, exit_array)

print(nodes["C"].exit, nodes["C"].next_node)
