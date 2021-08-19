import jsonPy_global
import json
import glob


def load_paths():
    paths = []
    for path in glob.glob("../jsons/*.json"):
        paths.append(str(path).split("/")[-1])
    jsonPy_global.json_paths = paths


def read_json(file_name):
    with open("../jsons/" + file_name, "r") as file:
        _jsondata = json.loads(file.read())

    # in json datas get 0. index as main key
    jsonPy_global.jsondata = _jsondata[list(_jsondata.keys())[0]]


def reverse_json_byvalue(value):
    for data in jsonPy_global.jsondata:
        for key, val in data.items():
            if value == val:
                print(str(list(jsonPy_global.jsondata).index(data)))
                return jsonPy_global.jsondata[list(jsonPy_global.jsondata).index(data)]
