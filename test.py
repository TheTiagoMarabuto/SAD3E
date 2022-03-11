from dijkstra import *
from node import *

edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
]

exit_array = ["E", "G"]

g = build_graph(edges)

nodes = read_nodes_from_graph(g, exit_array)

for node in nodes:
    print(node.node_name, "->", node.next_node, "To exit ->", node.distance_to_exit)