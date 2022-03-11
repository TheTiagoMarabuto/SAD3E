from dijkstra import *
from Node import *

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

nodes = []
for node in g:
    nodes.append(Node(node))

for i in range(len(nodes)):
    exit = near_exit(g, nodes[i].node_name, exit_array)
    if exit == nodes[i].node_name:
        nodes[i].distance_to_exit=0
        nodes[i].next_node = None
    else:
        d, prev = dijkstra(g, nodes[i].node_name, exit)
        path = find_path(prev, exit)
        nodes[i].next_node = next_node(path)
        nodes[i].distance_to_exit = d

for node in nodes:
    print(node.node_name, "->", node.next_node, "To exit ->", node.distance_to_exit)