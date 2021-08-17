from PyQt5.QtWidgets import QMainWindow, QToolBox, QVBoxLayout, QWidget

import jsonPy_global
from uis import toolboxMainUI
import functions


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.main_window = QMainWindow()
        self.setWindowTitle("Table Widget")
        self.tool_box = QToolBox()
        self.init_ui()

    def init_ui(self):
        self.main_window = toolboxMainUI.UIMainWindow()
        self.main_window.setup_ui(self)
        self.main_window.horizontal_lay.addWidget(self.tool_box)
        self.init_tbox()
        page = QWidget()
        self.tool_box.addItem(page, "page 1")
        self.tb_lay = QVBoxLayout(self.tool_box)
        self.tb_lay.addWidget(self.tool_box)


    def init_tbox(self):
        datas = jsonPy_global.jsondata["feeds"]
        for i in range(len(datas)):
            page = QWidget()
            for j in range(len(datas[i].keys())):
                self.tool_box.addItem(page, str(j))
        self.tb_lay.addWidget(self.tool_box)

