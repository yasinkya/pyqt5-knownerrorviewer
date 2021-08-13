from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
import uis.mainUI
import functions
import jsonPy_global


class New(QMainWindow):
    def __init__(self, x, y, w, h):
        super(New, self).__init__()
        # cannot let resize the window
        self.setFixedSize(w, h)
        self.setGeometry(x, y, w, h)
        self.setWindowTitle("Main")

        self.init_ui()

    def init_ui(self):
        jsonPy_global.jsondata = functions.read_json()
        # set mainui to window
        self.mainUI = uis.mainUI.Ui_MainWindow()
        self.mainUI.setupUi(self)

        some_label = QLabel(self)
        some_label.setObjectName("kek")

        xx = self.findChild(type(QLabel))

        # tabWidget
        self.tab = self.mainUI.tabWidget

        # sync qtabwidget
        self.sync_tabs(jsonPy_global.jsondata)
        # tabbar clicked- idx current index of clicked tab
        # jsonPy_global.tablay = QVBoxLayout()
        self.tab.currentChanged.connect(lambda idx: self.tab_changed(jsonPy_global.jsondata["feeds"][idx], idx))
        self.tab_changed(jsonPy_global.jsondata["feeds"][0], 0)

    # Add tabs and change the their text's through json
    def sync_tabs(self, data):
        for i in data["feeds"]:
            tab = QWidget()
            self.tab.addTab(tab, str(i["id"]))

    # clicked tabbar
    def tab_changed(self, data, currenttab_idx):
        tablay = QVBoxLayout()
        print(tablay)

        functions.newtab(tablay, data.keys(), currenttab_idx)

        if not self.tab.currentWidget().layout():
            self.tab.currentWidget().setLayout(tablay)
