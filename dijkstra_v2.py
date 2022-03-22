# @author - Tiago Marabuto
import math
from collections import defaultdict

from fibheap import *


class Node:
    def __init__(self, name=None, location=None, next_node=None, distance_to_exit=1806199818061998, exit=None):
        self.name = name
        self.next_node = next_node
        self.distance_to_exit = distance_to_exit
        # --TEMPORARY EXIT VARIABLE-- #
        self.exit = exit
        # --------------------------- #
        self.edges = []
        self.location = location  # node (x, y, z), with z being the floor in which the node is located

    def set_distance(self, distance_to_exit):
        self.distance_to_exit = distance_to_exit

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_distance(self):
        return self.distance_to_exit

    def get_next_node(self):
        return self.next_node

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location


# build graph given edges dictionary. Returns list of Node objects
def build_graph(edges):
    nodes = defaultdict(Node)
    seen_edges = defaultdict(int)
    for src in edges:
        for dst, weight, hazard in zip(edges.get(src).get("dst"), edges.get(src).get("weight"),
                                       edges.get(src).get("hazard")):
            seen_edges[(src, dst)] += 1
            if seen_edges[(src, dst)] > 1:  # checking for duplicated edge entries
                continue
            nodes[src].edges.append((dst, weight, hazard))
            # nodes[dst].edges.append((src, weight, hazard))
        nodes[src].location = edges.get(src).get("location")
        nodes[src].name = src
    return nodes


# calculates distance from src_node to all nodes. returns distance dictionary
def dijkstra_distance(nodes, src_node):
    dist = dict()
    prev = dict()
    for node in nodes:
        dist[node] = float('inf')
        prev[node] = None

    dist[src_node] = 0

    heap = makefheap()
    for node in nodes:
        fheappush(heap, (dist[node], node))

    while heap.num_nodes:
        u = fheappop(heap)
        for dst, weight, hazard in nodes[u[1]].edges:
            if dist[dst] > dist[u[1]] + weight * hazard:
                dist[dst] = dist[u[1]] + weight * hazard
                prev[dst] = u[1]

    # SEE IF DECREASE_KEY(H,V) MAKES ANY DIFFERENCE (see OneNote pseudocode)
    ## CHECK WITH BIGGER GRAPHS, SMALL GRAPHS DON'T SHOW DIFFERENCE
    return dist, prev


# Set nearest exit and next node
def set_nearest_exit(nodes, exit_array):
    for exit in exit_array:
        distance, prev = dijkstra_distance(nodes, exit)
        for node in nodes:
            path = find_path(prev, node)
            if nodes[node].get_distance() > distance[node]:
                nodes[node].set_distance(distance[node])
                nodes[node].exit = exit
                # print(node, exit, path)
                if exit != node:
                    nodes[node].set_next_node(path[1])
                else:
                    nodes[node].set_next_node(path[0])


def distance_between_nodes(nodeA, nodeB):
    if nodeA.location[2] == nodeB.location[2]:
        return math.sqrt((nodeA.location[0] - nodeB.location[0]) ** 2 + (nodeA.location[1] - nodeB.location[1]) ** 2)
    else:
        print("Can't calculate distance between: ", nodeA, "and", nodeB)


def change_hazard_intensity(nodeA, nodeB, hazard_intensity):
    for dst, weight, hazard in nodeA.edges:
        if dst == nodeB.name:
            nodeA.edges.remove((dst, weight, hazard))
            nodeB.edges.remove((nodeA.name, weight, hazard))

            nodeA.edges.append((dst, weight, hazard_intensity))
            nodeB.edges.append((nodeA.name, weight, hazard_intensity))


def find_path(pr, node):  # generate path list based on parent points 'prev'
    p = []
    aux = node
    while aux is not None:
        p.append(aux)
        aux = pr[aux]
    return p  # [::-1]  # Inverted array
