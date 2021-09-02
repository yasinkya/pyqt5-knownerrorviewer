from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QSizePolicy, QPushButton, QToolButton
from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.UIs.GzIS_main_window import Ui_MainWindow
from GzIS_Error.classes import table_widget_target, table_widget_tests, TabBar, ComboBox


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close = QToolButton()
        self.setupUi(self)


    def setupUi(self, MainWindow):
        super().setupUi(self)

        # Custom tilebar actions - close
        self.btn_close.setText("x")
        self.btn_close.setStyleSheet("QToolButton{ background-color: red; color: white; font-size: 17px;"
                                     "min-width: 1em; max-height: 1em;}")
        self.btn_close.clicked.connect(self.close)
        self.tilebar_custom.setCornerWidget(self.btn_close)
