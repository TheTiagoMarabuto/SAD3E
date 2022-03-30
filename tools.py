# @author - Tiago Marabuto

import json
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import pylab


# creates JSON file with name = filename
def create_json_file(filename):
    try:
        file = open(filename, 'r')
        print("File already exists")
        file.close()
    except IOError:
        file = open(filename, 'w')
        file.close()


# writes dictionary to file with name filename
def write_json(filename, mode, dict):
    file = open(filename, mode)
    string = str(dict)
    json.dump(string, file, indent=2)
    file.close()


# reads from filename and returns a dictionary
def read_json(filename):
    file = open(filename, "r")
    aux = json.load(file)
    file.close()
    return aux


def draw_graph(graph):
    G = nx.Graph()
    for node in graph:
        G.add_node(node, pos=graph[node].location[0:2])
    seen_edges = defaultdict(int)
    for node in graph:
        for dst, weight, hazard in graph[node].edges:
            seen_edges[(node, dst)] += 1
            seen_edges[(dst, node)] += 1
            if seen_edges[(node, dst)] > 1:  # checking for duplicated edge entries
                continue
            G.add_edge(node, dst, weight=weight * hazard)

    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=4, verticalalignment='top')
    nx.draw(G, pos, node_size=180, with_labels=True, edge_cmap=plt.cm.Reds, font_size = 8)
    pylab.show()
