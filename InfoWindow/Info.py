from PyQt5.QtWidgets import QMainWindow
from uis import info_ui as window_ui


class New(QMainWindow):
    def __init__(self, data):
        super(New, self).__init__()
        self.mw = window_ui.Ui_MainWindow()
        self.init_ui(data)

    def init_ui(self, data):
        self.mw.setupUi(self)
        self.mw.plainTextEdit.setPlainText(data)
        self.mw.plainTextEdit.setReadOnly(True)
