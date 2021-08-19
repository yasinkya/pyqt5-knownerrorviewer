from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTabWidget
import uis.mainUI
import functions
import jsonPy_global


class New(QMainWindow, uis.mainUI.UiMainWindow):
    def __init__(self, w, h):
        super(New, self).__init__()
        self.setMinimumSize(w, h)
        self.setWindowTitle("Main")
        self.mainUI = QMainWindow()
        self.tabwid_main = QTabWidget()
        self.init_ui()

    def init_ui(self):
        # set mainui to window
        self.mainUI = uis.mainUI.UiMainWindow()
        self.mainUI.setup_ui(self)
        # tabWidget define

        self.tabwid_main = self.mainUI.tabWidget
        with open("../uis/tabwid_sheet.css", "r") as file:
            self.tabwid_main.setStyleSheet(file.read())

        # sync qtabwidget
        self.sync_tabs(jsonPy_global.jsondata)
        # tabbar clicked- idx current index of clicked tab
        self.tabwid_main.currentChanged.connect(lambda idx: self.init_tab(jsonPy_global.jsondata[idx]))

        # set current clicked
        self.init_tab(jsonPy_global.jsondata[0])

    # Add tabs and change the their text's through json
    def sync_tabs(self, data):
        for i in data:
            self.tabwid_main.addTab(QWidget(), str(i["id"]))

    # clicked tabbar
    def init_tab(self, data):
        # TODO: when u clicked a tab, its create a new down tab but whats happening the old tab
        if not self.tabwid_main.currentWidget().layout():
            tabmain_lay = QVBoxLayout(self.tabwid_main.currentWidget())
            functions.newtab(tabmain_lay, self.tabwid_main.currentWidget(), data)

