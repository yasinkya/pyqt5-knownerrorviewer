from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget, QLabel, QSizePolicy, QGridLayout, QPlainTextEdit
import json
import jsonPy_global


def read_json():
    f = open("jsons/employee.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def newtab(layout: QVBoxLayout, tab_main: QWidget, keys: set, currenttab_idx):
    # define a new tabwidget then add this to up tabwidget's layout
    tabwid_child = QTabWidget(tab_main)

    # the tablist is the name of the tabs to be created
    for i in keys:
        tab_child = QWidget()
        tabwid_child.addTab(tab_child, i)


    layout.addWidget(tabwid_child)

    # then define a new layout for added tabwidget
    # newtab_lay = QVBoxLayout()




    if not tab_child.layout():
        tabchild_lay = QGridLayout(tab_child)


    # set click signal for created tabs & set their layout
    tabwid_child.currentChanged.connect(lambda: tabchanced(tabwid_child, jsonPy_global.jsondata["feeds"]))

    # if not tabwid.currentWidget().layout():
    #     tabwid.currentWidget().setLayout(newtab_lay)


def tabchanced(clickedtab: QTabWidget, data):
    # todo: ram usage for created tabs click
    # todo: define layout for tabwidget and then add to another one gridlayout as child

    if not clickedtab.currentWidget().layout():
        tabchild_lay = QGridLayout(clickedtab.currentWidget())

    plaintext = QPlainTextEdit(clickedtab.currentWidget())
    # plaintext.setReadOnly(True)
    plaintext.setPlainText(str(data))

    clickedtab.currentWidget().layout().addWidget(plaintext, 0, 0, 1, 1)
    """
    gridlayout = QGridLayout(clickedtab)
    label = QLabel()
    gridlayout.addWidget(label)
    sizepolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizepolicy.setVerticalPolicy(0)
    sizepolicy.setHorizontalPolicy(0)
    sizepolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
    label.setSizePolicy(sizepolicy)
    label.setText(str(data))
    """

    # print(clickedtab is jsonPy_global.current_clicked_up_tab)
    # print(data)

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