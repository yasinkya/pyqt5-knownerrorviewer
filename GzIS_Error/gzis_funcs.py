import glob
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox
from GzIS_Error import global_variables
from classes import Main_Window


def read_paths():
    paths = []
    for path in glob.glob(f"{global_variables.jsons_folder}/*"):
        paths.append(str(path).split("/")[-1].split(".")[0])
    global_variables.json_paths = paths


def cbx_chooser_changed(idx, self: QComboBox):
    with open(f"{global_variables.jsons_folder}/{self.currentText()}.json", "r") as json_file:
        global_variables.jsondata = json.loads(json_file.read())["testSuites"]
    for key in global_variables.jsondata.keys():
        global_variables.json_keys.append(key)


def set_keys(self: QComboBox):

    with open(f"{global_variables.jsons_folder}/{self.currentText()}.json", "r") as json_file:
        global_variables.jsondata = json.loads(json_file.read())["testSuites"]
    for key in global_variables.jsondata.keys():
        global_variables.json_keys.append(key)
