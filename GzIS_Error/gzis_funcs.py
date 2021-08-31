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


def isaccepted_filter(table: QTableWidget, isaccept):
    failed_tests: QTreeWidget
    if not isaccept == "All":

        # re_filter(table)
        x = 0
        for row in range(table.rowCount()):
            failed_tests = table.cellWidget(row, 2)
            count = 0
            for top in range(failed_tests.topLevelItemCount()):
                if failed_tests.topLevelItem(top - count).child(1).text(0) not in f"isAccepted: {isaccept}":
                    print(f"{failed_tests.takeTopLevelItem(top - count).text(0)} was removed")
                    count += 1

    else:
        re_filter(table)


def re_filter(table: QTableWidget):
    failed_tests: QTreeWidget
    for i in global_variables.filter_elements.keys():
        failed_tests = table.cellWidget(global_variables.filter_elements[i][0], 2)
        failed_tests.addTopLevelItem(global_variables.filter_elements[i][1])
    global_variables.filter_elements.clear()


    # for row in range(table.rowCount()):
    #     failed_tests = table.cellWidget(row, 2)
    #     failed_tests.insertTopLevelItems(0, global_variables.filter_elements)


"""
***********************v3 - find willremove items
            for top in range (t.topLevelItemCount()):
                for rm in willremove:
                    if t.topLevelItem(top).text(0) == t.topLevelItem(rm).text(0): 
                        print(t.topLevelItem(top).text(0))
            
            
            *************************************
    for top in range(t.topLevelItemCount()):
        print(t.topLevelItem(top).text(0))    
        for chi in range(t.topLevelItem(top).childCount()):
            print(t.topLevelItem(top).child(chi).text(0))  
            
         -> test3
                -> failType: Fail
                    isAccept: false   
                    
                    
                    
                    -------------------- v2 
                    
                                for top in range(failed_tests.topLevelItemCount()):
    for chi in range(failed_tests.topLevelItem(top).childCount()):
        if failed_tests.topLevelItem(top).child(chi).text(0) in "isAccepted: True":
            print(failed_tests.topLevelItem(top).child(chi).text(0))

        else:
            print("Not False")
            
        ***********************************************************   ********
        
         if not isaccept == "All":

        # re_filter(table)
        x = 0
        for row in range(table.rowCount()):
            failed_tests = table.cellWidget(row, 2)
            for top in range(failed_tests.topLevelItemCount()):
                for chi in range(failed_tests.topLevelItem(top).childCount()):
                    if failed_tests.topLevelItem(top).child(chi).text(0) in f"isAccepted: {not bool(isaccept)}":
                        # print(f"\n -> {failed_tests.topLevelItem(top).text(0)}")
                        # print(f"\t -> {failed_tests.topLevelItem(top).child(chi).text(0)} is removing")
                        willremove.append(top)
                        global_variables.filter_elements[x] = [row, failed_tests.topLevelItem(top)]
                        x += 1

        i = 0
        print(willremove)
        for rm in willremove:
            rm -= i
            for top in range(failed_tests.topLevelItemCount()):
                if top == rm:
                    # print(f"{failed_tests.topLevelItem(top).text(0)} is removing")
                    print(f"{failed_tests.takeTopLevelItem(top).text(0)} was removed")
                    # willremove.remove(rm)
                    i += 1


    else:
        re_filter(table)    
            
                    
"""