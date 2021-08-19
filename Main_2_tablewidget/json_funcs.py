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


# "2020-01-02T10:35:11.7588502"
def reverse_json(value):
    val_key = ""
    for data in jsonPy_global.jsondata:
        for key, val in data.items():
            # val_key = key if val == value else ""
            if value == val:
                val_key = key
                for dt in jsonPy_global.jsondata:
                    if dt[val_key] == value:
                        print(str(list(jsonPy_global.jsondata).index(dt)))



def blabla():
    show_jsons()
    read_json(jsonPy_global.json_paths[1])


blabla()
reverse_json(jsonPy_global.jsondata[1]["createdAt"])
