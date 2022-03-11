
class Node:
    def __init__(self, node_name):
        self.node_name = node_name
        self.next_node = None
        self.distance_to_exit = 1806199818061998

    def updateNode(self, path, distance):
        self.next_node = path[1]
        self.distance_to_exit = distance

