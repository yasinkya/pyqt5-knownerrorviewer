from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtWidgets
from GzIS_Error.classes import ComboBox, Tabwidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget()
        self.menubar = QtWidgets.QMenuBar()
        self.statusbar = QtWidgets.QStatusBar()
        self.main_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.cbx_chooser = ComboBox.New()
        self.cbx_paths = ComboBox.New()
        self.tabWidget = Tabwidget.New()
        self.setup_ui()

    def setup_ui(self):
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 24))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.centralwidget.setObjectName("centralwidget")
        self.main_layout.setObjectName("gridLayout")
        self.cbx_chooser.setObjectName("comboBox_2")
        self.main_layout.addWidget(self.cbx_chooser, 0, 1, 1, 1)
        self.main_layout.addWidget(self.cbx_paths, 0, 0, 1, 1)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cbx_paths.sizePolicy().hasHeightForWidth())
        self.cbx_paths.setSizePolicy(size_policy)
        self.cbx_paths.setObjectName("comboBox")

        self.tabWidget.setMinimumSize(QtCore.QSize(720, 360))
        self.tabWidget.setObjectName("tabWidget")
        self.main_layout.addWidget(self.tabWidget, 1, 0, 1, 2)
        self.setCentralWidget(self.centralwidget)
        # with open("UIs/GzIS_tabwid_styel_sheet.css", "r") as twsheet:
        #     self.tabWidget.setStyleSheet(str(twsheet.read()))



        self.retranslate_ui()
        # self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
