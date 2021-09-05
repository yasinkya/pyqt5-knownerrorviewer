# import global_variables
import json
import glob
import global_variables as globvar


def read_paths():
    for path in glob.glob(f"{globvar.folder}/*"):
        if str(path).split("/")[-1] in "summary-info":
            continue
        globvar.json_paths.append(str(path).split("/")[-1])


def read_json(file_name):
    with open("../jsons/" + file_name, "r") as file:
        _jsondata = json.loads(file.read())

    # in json datas get 0. index as main key
    globvar.current_jsondata = _jsondata[list(_jsondata.keys())[0]]


def reverse_json_byvalue(value):
    for data in globvar.current_jsondata:
        for key, val in data.items():
            if value == val:
                print(str(list(globvar.current_jsondata).index(data)))
                return globvar.current_jsondata[list(globvar.current_jsondata).index(data)]
