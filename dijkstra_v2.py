# @author - Tiago Marabuto
# based on source code from Ran Ding (https://gist.github.com/dingran/b827b65a252000e25d818ba3520242e1)
from collections import defaultdict
from fibheap import *


class Node:
    def __init__(self, next_node=None, distance_to_exit=1806199818061998, exit=None):
        self.next_node = next_node
        self.distance_to_exit = distance_to_exit
        # --TEMPORARY EXIT VARIABLE-- #
        self.exit = exit
        # --------------------------- #
        self.edges = []

    def set_distance(self, distance_to_exit):
        self.distance_to_exit = distance_to_exit

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_distance(self):
        return self.distance_to_exit

    def get_next_node(self):
        return self.next_node


def build_graph(edges):
    nodes = defaultdict(Node)
    seen_edges = defaultdict(int)
    for src, dst, weight in edges:
        seen_edges[(src, dst, weight)] += 1
        if seen_edges[(src, dst, weight)] > 1:  # checking for duplicated edge entries
            continue
        nodes[src].edges.append((dst, weight))
        nodes[dst].edges.append((src, weight))
    return nodes


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
        for dst, weight in nodes[u[1]].edges:
            if dist[dst] > dist[u[1]] + weight:
                dist[dst] = dist[u[1]] + weight
                prev[dst] = u[1]

    # SEE IF DECREASE_KEY(H,V) MAKES ANY DIFFERENCE (OneNote pseudo code)
    return dist


def choose_nearest_exit(nodes, exit_array):
    for exit in exit_array:
        for node, distance in dijkstra_distance(nodes, exit):
            if nodes[node].get_distance() > distance:
                nodes[node].set_distance(distance)
                nodes[node].exit = exit
