import jsonPy_global
import json
import glob


def show_jsons():
    for path in glob.glob("../jsons/*.json"):
        return str(path).split("/")[-1]


def read_json(path):
    with open(path, "r") as file:
        _jsondata = json.loads(file.read())
    # in json datas get 0. index as main key
    # for employee.json -> data: json["feeds]
    jsonPy_global.jsondata = _jsondata[list(_jsondata.keys())[0]]


def reverse_json(path):
    pass


print(show_jsons())