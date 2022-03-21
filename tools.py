# @author - Tiago Marabuto

import json


# -------------- NO NEED ------------------------------------
# edges type -> list; edge_dict type -> dictionary          |
# function to turn dictionary of edges in edge list         |
def dict_toList(edges, edge_dict):
    for src_node in edge_dict:
        for dst, weight in zip(edge_dict.get(src_node).get("dst"), edge_dict.get(src_node).get("weight")):
            edges.append((src_node, dst, weight))


# edges type -> list; edge_dict type -> dictionary          |
# function to turn edge list in dictionary of edges         |
def list_toDict(edges, edge_dict):
    for src, dst, weight in edges:
        if src in edge_dict.keys():
            if dst not in edge_dict.get(src).get("dst"):
                edge_dict.get(src).get("dst").append(dst)
                edge_dict.get(src).get("weight").append(weight)
        else:
            edge_dict.update({src: {
                "dst": [dst],
                "weight": [weight]
            }
            })

#                                                           |
# -----------------------------------------------------------


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
