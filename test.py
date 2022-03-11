from dijkstra import *
from node import *
from read_excel import *

loc = "/Users/tiagomarabuto/PycharmProjects/SAD3E/graph.xls"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# edges = [
# ("A", "B", 7),
# ("A", "D", 5),
# ("B", "C", 8),
# ("B", "D", 9),
# ("B", "E", 7),
# ("C", "E", 5),
# ("D", "E", 15),
# ("D", "F", 6),
#  ("E", "F", 8),
#   ("E", "G", 9),
#    ("F", "G", 11)
# ]
edges = []
fires = []
exit_array = ["XX"]
read_excel(sheet, edges)

while 1:

    g = build_graph(edges)

    nodes = read_nodes_from_graph(g, exit_array)

    if input("Do you want to print the graph? (y/n) ") == "y":
        for node in nodes:
            print("Node:", node.node_name, "\tNext_Node:", node.next_node, "\tDistance:", node.distance_to_exit)

    elif input("Do you want to add a fire? (y/n) ") == "y":
        a, b = input("Enter two nodes: ").split()
        fires = insert_fire(edges, a, b)
    elif input("Do you want to put out a fire? (y/n) ") == "y":
        a, b = input("Enter two nodes: ").split()
        put_out_fire(fires, edges, a, b)
    elif input("Do you wan to end the simulation? (y/n ") == "y":
        print("Ending Simulation...")
        break
