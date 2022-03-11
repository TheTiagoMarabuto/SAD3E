from dijkstra import *


class Node:
    def __init__(self, node_name):
        self.node_name = node_name
        self.next_node = None
        self.distance_to_exit = 1806199818061998

    def updateNode(self, path, distance):
        self.next_node = path[1]
        self.distance_to_exit = distance


def read_nodes_from_graph(graph, exit_array):
    nodes = []
    for node in graph:
        nodes.append(Node(node))

    for i in range(len(nodes)):
        exit = near_exit(graph, nodes[i].node_name, exit_array)
        if exit == nodes[i].node_name:
            nodes[i].distance_to_exit = 0
            nodes[i].next_node = None
        else:
            d, prev = dijkstra(graph, nodes[i].node_name, exit)
            path = find_path(prev, exit)
            nodes[i].next_node = next_node(path)
            nodes[i].distance_to_exit = d
    return nodes


def insert_fire(edges, pointA, pointB):
    fire = []
    for src, dst, weight in edges:
        if (src == pointA and dst == pointB) or (src == pointB and dst == pointA):
            if(weight == float('inf')):
                print("There was already a fire")
            edges.remove((src, dst, weight))
            edges.append((src, dst, float('inf')))
            print("Fire Added between", src, "and", dst)
            fire.append((src, dst, weight))
    return fire


def put_out_fire(fire, edges, pointA, pointB):
    for src, dst, weight in fire:
        if (src == pointA and dst == pointB) or (src == pointB and dst == pointA):
            for src1, dst1, weight1 in edges:
                if ((src1 == pointA and dst1 == pointB) or (src1 == pointB and dst1 == pointA)) and (
                        weight1 == float('inf')):
                        edges.remove((src1, dst1, weight1))
                        edges.append((src1, dst1, weight))
                        fire.remove((src, dst, weight))
                        print("Fire Put out between", src, "and", dst)
