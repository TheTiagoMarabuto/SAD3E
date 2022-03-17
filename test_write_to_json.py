import string as st
from random import *
import random
from json_read_write import *


def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(st.ascii_letters) for i in range(length))
    return result_str


filename = "test_json.json"
create_json_file(filename)

json_file = open(filename, "w")
string = []
for i in range(3):
    a = get_random_string(5)
    b = get_random_string(5)
    w = randint(1, 20)
    string.append([a, b, w])


write_to_json(json_file, string)
json_file.close()

json_file = open(filename, "r")

print(read_json(json_file))
json_file.close()