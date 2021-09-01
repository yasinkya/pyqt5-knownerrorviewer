import glob
import json
from PyQt5.QtWidgets import QComboBox, QTabBar, QTableWidget, QTreeWidget
from GzIS_Error import global_variables


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        if str(path).split("\\")[-1] in "summary-info":
            continue
        global_variables.json_paths.append(str(path).split("\\")[-1])


def sync_global_jsonfiles(combo_box: QComboBox):
    global_variables.current_path = f"{global_variables.folder}"
    global_variables.json_files.clear()
    for file in glob.glob(f"{global_variables.folder}/{combo_box.currentText()}/*.json"):
        global_variables.json_files.append(str(file).split("\\")[-1])


def set_tabbar(json_path, tabbar: QTabBar, target: bool):
    if not target:
        with open(json_path, "r") as file:
            global_variables.current_jsondata = json.loads(file.read())["testSuites"]
    else:
        with open(json_path, "r") as file:
            global_variables.current_jsondata = json.loads(file.read())["Target"]

    for key in global_variables.current_jsondata.keys():
        tabbar.addTab(key)


def isaccepted_filter(table: QTableWidget, isaccept):
    failed_tests: QTreeWidget
    if not isaccept == "All":
        re_filter(table)
        for row in range(table.rowCount()):
            count = 0
            failed_tests = table.cellWidget(row, 2)
            for top in range(failed_tests.topLevelItemCount()):
                if failed_tests.topLevelItem(top - count).child(1).text(0) not in f"isAccepted: {isaccept}":
                    global_variables.filter_elements[f"{row}-{top}"] = failed_tests.topLevelItem(top - count)
                    print(f"{failed_tests.takeTopLevelItem(top - count).text(0)} was removed")
                    count += 1
    else:
        re_filter(table)


def re_filter(table: QTableWidget):
    for key, val in global_variables.filter_elements.items():
        table.cellWidget(int(key.split("-")[0]), 2).addTopLevelItem(val)
    global_variables.filter_elements.clear()
