# @author - Tiago Marabuto
import heapq
import math
from collections import defaultdict
import heapq as hq
from fibheap import *

BIGINT = 1806199818061998


class Node:
    def __init__(self, name=None, location=None, next_node=None, distance_to_exit=BIGINT, exit=None):
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
    graph = defaultdict(Node)
    seen_edges = defaultdict(int)
    for src in edges:
        for dst, weight, hazard in zip(edges.get(src).get("dst"), edges.get(src).get("weight"),
                                       edges.get(src).get("hazard")):
            seen_edges[(src, dst)] += 1
            # seen_edges[(dst,src)] += 1
            if seen_edges[(src, dst)] > 1:  # checking for duplicated edge entries
                continue
            graph[src].edges.append((dst, weight, hazard))
            # print(src, dst, weight, hazard)
            # graph[dst].edges.append((src, weight, hazard))
        graph[src].location = edges.get(src).get("location")
        graph[src].name = src
    return graph


# calculates distance from src_node to all nodes. returns distance dictionary
def dijkstra_distance(graph, src_node):
    dist = dict()
    prev = dict()
    for node in graph:
        dist[node] = float('inf')
        prev[node] = None

    dist[src_node] = 0

    heap2 = [(dist[src_node], src_node)]
    seen = set()
    while heap2:
        dist1, node = heapq.heappop(heap2)
        if node not in seen:
            seen.add(node)
            for dst, weight, hazard in graph[node].edges:
                if dist[dst] > dist[node] + weight * hazard:
                    dist[dst] = dist[node] + weight * hazard
                    prev[dst] = node
                    heapq.heappush(heap2, (dist[dst], dst))

    return dist, prev


# Set nearest exit and next node
def set_nearest_exit(graph, exit_array):
    for exit in exit_array:
        distance, prev = dijkstra_distance(graph, exit)
        for node in graph:
            path = find_path(prev, node)
            # print(node, graph[node].get_distance(), distance[node])
            if graph[node].get_distance() > distance[node]:
                graph[node].set_distance(distance[node])
                graph[node].exit = exit
                # print(node, exit, path)
                if exit != node:
                    graph[node].set_next_node(path[1])
                    # print(node, "nextnode", graph[node].set_next_node(path[1]))
                else:
                    graph[node].set_next_node(path[0])


def distance_between_nodes(nodeA, nodeB):
    if nodeA.location[2] == nodeB.location[2]:
        return math.sqrt((nodeA.location[0] - nodeB.location[0]) ** 2 + (nodeA.location[1] - nodeB.location[1]) ** 2)
    else:
        print("Can't calculate distance between: ", nodeA, "and", nodeB)


def change_hazard_intensity(nodeA, nodeB, hazard_intensity, graph, exit_array):
    for dst, weight, hazard in nodeA.edges:
        if dst == nodeB.name:
            nodeA.edges.remove((dst, weight, hazard))
            nodeB.edges.remove((nodeA.name, weight, hazard))

            nodeA.edges.append((dst, weight, hazard_intensity))
            nodeB.edges.append((nodeA.name, weight, hazard_intensity))

            nodeA.set_distance(BIGINT)
            nodeB.set_distance(BIGINT)

            set_nearest_exit(graph, exit_array)


def find_path(pr, node):  # generate path list based on parent points pr and the node name
    p = []
    aux = node
    while aux is not None:
        p.append(aux)
        aux = pr[aux]
    return p  # [::-1]  # Inverted array
