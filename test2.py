from dijkstra import *
from tools import *

edges = {
    "A": {
        "dst": ["B", "X", "Y"],
        "weight": [20, 14, 14],
        "hazard": [1, 1, 1],
        "location": (20, 170, 0)
    },
    "C": {
        "dst": ["D", "Z", "AA"],
        "weight": [20, 14, 14],
        "hazard": [1, 1, 1],
        "location": (50, 170, 0)
    },
    "F": {
        "dst": ["G", "BB", "CC"],
        "weight": [20, 14, 14],
        "hazard": [1, 1, 1],
        "location": (80, 170, 0)
    },
    "I": {
        "dst": ["J", "DD", "EE"],
        "weight": [20, 14, 14],
        "hazard": [1, 1, 1],
        "location": (110, 170, 0)
    },
    "W": {
        "dst": ["V", "FF", "GG"],
        "weight": [20, 14, 14],
        "hazard": [1, 1, 1],
        "location": (170, 170, 0)
    },
    "B": {
        "dst": ["A", "E", "X", "Y"],
        "weight": [20, 36, 14, 14],
        "hazard": [1, 1, 1, 1],
        "location": (20, 140, 0)
    },
    "D": {
        "dst": ["C", "E", "Z", "AA"],
        "weight": [20, 10, 14, 14],
        "hazard": [1, 1, 1, 1],
        "location": (50, 140, 0)
    },
    "G": {
        "dst": ["F", "H", "BB", "CC"],
        "weight": [20, 10, 14, 14],
        "hazard": [1, 1, 1, 1],
        "location": (80, 140, 0)
    },
    "J": {
        "dst": ["I", "J", "DD", "EE"],
        "weight": [20, 10, 14, 14],
        "hazard": [1, 1, 1, 1],
        "location": (110, 140, 0)
    },
    "V": {
        "dst": ["W", "U", "FF", "GG"],
        "weight": [20, 10, 14, 14],
        "hazard": [1, 1, 1, 1],
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
    },
    "X": {
        "dst": ["A", "B"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (10, 155, 0)
    },
    "Y": {
        "dst": ["A", "B"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (30, 155, 0)
    },
    "Z": {
        "dst": ["C", "D"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (40, 155, 0)
    },
    "AA": {
        "dst": ["C", "D"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (60, 155, 0)
    },
    "BB": {
        "dst": ["F", "G"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (70, 155, 0)
    },
    "CC": {
        "dst": ["F", "G"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (90, 155, 0)
    },
    "DD": {
        "dst": ["I", "J"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (100, 155, 0)
    },
    "EE": {
        "dst": ["I", "J"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (120, 155, 0)
    },
    "FF": {
        "dst": ["W", "V"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (160, 155, 0)
    },
    "GG": {
        "dst": ["W", "V"],
        "weight": [14, 14],
        "hazard": [1, 1],
        "location": (180, 155, 0)
    }

}

exit_array = ["S", "U"]
graph = build_graph(edges)
set_nearest_exit(graph, exit_array)