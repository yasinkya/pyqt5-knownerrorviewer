import jsonPy_global
import json
import glob


def show_jsons():
    paths = []
    for path in glob.glob("../jsons/*.json"):
        paths.append(str(path).split("/")[-1])
    jsonPy_global.json_paths = paths


def read_json(path):
    with open("../jsons/"+path, "r") as file:
        _jsondata = json.loads(file.read())
    # in json datas get 0. index as main key
    # for employee.json -> data: json["feeds]
    jsonPy_global.jsondata = _jsondata[list(_jsondata.keys())[0]]


def reverse_json(path):
    pass


def blabla():
    show_jsons()
    read_json(jsonPy_global.json_paths[3])
    print(jsonPy_global.jsondata)


blabla()