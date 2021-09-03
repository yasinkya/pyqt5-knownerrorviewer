from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QObject, QEvent
from PyQt5.QtGui import QColor, QPalette, QPixmap, QIcon, QDragMoveEvent
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QSizePolicy, QPushButton, QToolButton
import global_variables, gzis_funcs
from UIs.GzIS_main_window import Ui_MainWindow
from classes import table_widget_target, table_widget_tests, TabBar, ComboBox


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_close = QToolButton()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(self)

        # Custom tilebar actions - close
        self.btn_close.setText("x")
        self.btn_close.setStyleSheet("QToolButton{ background-color: rgb(45,45,40); color: #fffff0; font-size: 15px;"
                                     "min-width: 1.6em; max-height: 1.5em;"
                                     "}")
        self.btn_close.clicked.connect(self.close)
        self.tilebar_custom.setStyleSheet("QMenuBar{background-color: rgb(145,45,45); color: #fffff0}"
                                          "QMenu{background-color: rgb(70,70,70);}")
        self.tilebar_custom.setCornerWidget(self.btn_close)



    def eventFilter(self, obj: QObject, evn: QEvent):
        if obj == self.tilebar_custom:
            print(evn.type())
            if evn.type() ==2:
                print(obj)
                self.setWindowFlag(Qt.BypassGraphicsProxyWidget)
        return super().eventFilter(obj, evn)