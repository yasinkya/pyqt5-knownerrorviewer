import glob
import json
from PyQt5.QtWidgets import QComboBox
from GzIS_Error import global_variables


def read_paths():
    for path in glob.glob(f"{global_variables.jsons_folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


# def cbx_chooser_changed(idx, self: QComboBox):
#     with open(f"{global_variables.jsons_folder}/{self.currentText()}.json", "r") as json_file:
#         global_variables.jsondata = json.loads(json_file.read())["testSuites"]
#     for key in global_variables.jsondata.keys():
#         global_variables.json_keys.append(key)


def set_keys(self: QComboBox):
    jsons_files = glob.glob(f"{global_variables.jsons_folder}/{self.currentText()}/*.json")
    for files in glob.glob(f"{global_variables.jsons_folder}/{self.currentText()}/*.json"):
        pass
    # with open(f"{global_variables.jsons_folder}/{self.currentText()}.json", "r") as json_file:
    #     global_variables.jsondata = json.loads(json_file.read())["testSuites"]
    # for key in global_variables.jsondata.keys():
    #     global_variables.json_keys.append(key)
