from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QGridLayout
import uis.mainUI
import functions
import jsonPy_global


class New(QMainWindow):
    def __init__(self, x, y, w, h):
        super(New, self).__init__()
        # cannot let resize the window
        # self.setFixedSize(w, h)
        # self.setGeometry(x, y, w, h)
        self.setWindowTitle("Main")
        self.mainUI = QMainWindow()
        self.up_tabwdget = QWidget()
        self.init_ui()

    def init_ui(self):
        # set mainui to window
        self.mainUI = uis.mainUI.UiMainWindow()
        self.mainUI.setup_ui(self)

        # tabWidget define
        self.up_tabwdget = self.mainUI.tabWidget
        # sync qtabwidget
        self.sync_tabs(jsonPy_global.jsondata)
        # tabbar clicked- idx current index of clicked tab
        self.up_tabwdget.currentChanged.connect(lambda idx: self.tab_changed(jsonPy_global.jsondata["feeds"][idx], idx))
        self.tab_changed(jsonPy_global.jsondata["feeds"][0], 0)

    # Add tabs and change the their text's through json
    def sync_tabs(self, data):
        for i in data["feeds"]:
            tab = QWidget()
            self.up_tabwdget.addTab(tab, str(i["id"]))

    # clicked tabbar
    def tab_changed(self, data, currenttab_idx):
        tablay = QVBoxLayout()
        # TODO: when u clicked a tab, its create a new down tab but whats happening the old tab
        functions.newtab(tablay, data.keys(), currenttab_idx)

        # do not set defined layout to the current clicked tab again
        if not self.up_tabwdget.currentWidget().layout():
            self.up_tabwdget.currentWidget().setLayout(tablay)
