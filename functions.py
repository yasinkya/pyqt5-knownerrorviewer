from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget
import json
import jsonPy_global


def read_json():
    f = open("jsons/employee.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def newtab(layout: QVBoxLayout, tablist: set, currenttab_idx):

    tabwid = QTabWidget()
    layout.addWidget(tabwid)
    newtab_lay = QVBoxLayout()
    for i in tablist:
        tab = QWidget()
        tabwid.addTab(tab, i)
    tabwid.currentChanged.connect(lambda idx: tabchanced(tabwid, jsonPy_global.jsondata["feeds"][currenttab_idx]))
    tabwid.currentWidget().setLayout(newtab_lay)


def tabchanced(clickedtab: QTabWidget, data):

    print(data)

    """
        tablay = QVBoxLayout()
        tablist = set()
        print(tablist)
        print(tablay)
        print(clickedtab)
        tabList.add(i)
        if clickedTab.tabText(clickedTab.currentIndex())==str(i):
            #functions.newTab(tabLay,i["name"])
            list=set()
            for j in i:
                list.add(j)
            print(list)
            print(len(list))
            newTab(tabLay,list)
            break

        #tabLay.addWidget(lbl)
        #functions.newTab(tabLay)
        clickedTab.currentWidget().setLayout(tabLay) 
        """