from PyQt5.QtWidgets import QApplication, QMainWindow
from uis import info_ui as window_ui
import sys


class New(QMainWindow, window_ui):
    def __init__(self):
        super(New, self).__init__()
        self.mw = window_ui.Ui_MainWindow()
        self.init_ui(self, mw)

    def init_ui(self, mw):
        super().init_ui(mw)
