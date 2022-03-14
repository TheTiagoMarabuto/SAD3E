from node import *
from read_excel import *
import time
loc = "/Users/tiagomarabuto/PycharmProjects/SAD3E/graph.xls"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.nrows, sheet.ncols)
edges = []
fires = []
exit_array = ["XX"]
read_excel(sheet, edges)

# nos: 195
# arestas: 408

while 1:
    start = time.time()
    g = build_graph(edges)

    nodes = read_nodes_from_graph(g, exit_array)

    end = time.time()
    print(end - start, "s")

    if input("Do you want to print the graph? (y/n) ") == "y":
        for node in nodes:
            print("Node:", node.node_name, "\t\tNext_Node:", node.next_node, "\t\tDistance:", node.distance_to_exit)

    elif input("Do you want to add a fire? (y/n) ") == "y":
        a, b = input("Enter two nodes: ").split()
        fires = insert_fire(edges, a, b)
    elif input("Do you want to put out a fire? (y/n) ") == "y":
        a, b = input("Enter two nodes: ").split()
        put_out_fire(fires, edges, a, b)
    elif input("Do you wan to end the simulation? (y/n ") == "y":
        print("Ending Simulation...")
        break
