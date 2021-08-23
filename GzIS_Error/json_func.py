import global_variables
import json
import glob


def load_paths():
    paths = []
    for path in glob.glob("../jsons/*.json"):
        paths.append(str(path).split("/")[-1])
    global_variables.json_paths = paths


def read_json(file_name):
    with open("../jsons/" + file_name, "r") as file:
        _jsondata = json.loads(file.read())

    # in json datas get 0. index as main key
    global_variables.current_jsondata = _jsondata[list(_jsondata.keys())[0]]


def reverse_json_byvalue(value):
    for data in global_variables.current_jsondata:
        for key, val in data.items():
            if value == val:
                print(str(list(global_variables.current_jsondata).index(data)))
                return global_variables.current_jsondata[list(global_variables.current_jsondata).index(data)]
