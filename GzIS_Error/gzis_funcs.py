import glob
import json
from PyQt5.QtWidgets import QComboBox, QTabBar, QTableWidget, QTreeWidget
from GzIS_Error import global_variables


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


def sync_global_jsonfiles(combo_box: QComboBox):
    global_variables.current_path = f"{global_variables.folder}"
    for files in glob.glob(f"{global_variables.folder}/{combo_box.currentText()}/*.json"):
        global_variables.json_files.clear()
        global_variables.json_files.append(str(files).split("/")[-1])


def set_tabbar(json_path, tabbar: QTabBar):
    with open(json_path, "r") as file:
        global_variables.current_jsondata = json.loads(file.read())["testSuites"]

    for key in global_variables.current_jsondata.keys():
        tabbar.addTab(key)


def apply_filter(table: QTableWidget, isaccept):
    tree_failcount: QTreeWidget
    if isaccept:
        for row in range(table.rowCount()):
            tree_failcount = table.cellWidget(row, 2)
            # print(tree_failcount.topLevelItem(0).text(0))
            for top in range(tree_failcount.topLevelItem(0).childCount()):
                #tree_failcount.clear()
                print(tree_failcount)

            """
                for top in range(t.topLevelItemCount()):
                    print(t.topLevelItem(top).text(0))    
                    for chi in range(t.topLevelItem(top).childCount()):
                        print(t.topLevelItem(top).child(chi).text(0))  
                        
                     -> test3
                            -> failType: Fail
                                isAccept: false   
            """