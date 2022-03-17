import json


def create_json_file(filename):
    try:
        file = open(filename, 'r')
        print("File already exists")
        file.close()
    except IOError:
        file = open(filename, 'w')
        file.close()


def write_to_json(file, string):
    json.dump(string, file)


def read_json(file):
    data = []
    for line in file:
        data.append(json.loads(line))
    return data
