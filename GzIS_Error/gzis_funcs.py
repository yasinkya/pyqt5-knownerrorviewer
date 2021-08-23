import glob
import json
from PyQt5.QtWidgets import QComboBox
from GzIS_Error import global_variables


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


def sync_cbx_path(self: QComboBox):
    global_variables.current_path = f"{global_variables.folder}/{self.currentText()}"
    for files in glob.glob(f"{global_variables.folder}/{self.currentText()}/*.json"):
        global_variables.json_files.append(str(files).split("/")[-1].split(".")[0])

def cbx_changed():
    pass