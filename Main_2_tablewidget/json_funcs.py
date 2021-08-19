import json

import jsonPy_global
import jsons
import glob


def read_json(path):
    with open(path, "r") as file:
        jsonPy_global.jsondata = json.loads(file.read())

def reverse_json(path):
