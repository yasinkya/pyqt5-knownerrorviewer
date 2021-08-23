from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtWidgets

from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.classes import ComboBox, Tabwidget


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget()
        self.menubar = QtWidgets.QMenuBar()
        self.statusbar = QtWidgets.QStatusBar()
        self.main_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.cbx_paths = ComboBox.New()
        self.cbx_chooser = ComboBox.New()
        self.tabw_main = Tabwidget.New()
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(QtCore.QSize(800, 500))
        self.menubar.setObjectName("menubar")
        self.setGeometry(QtCore.QRect(0, 0, 592, 24))
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.main_layout.setObjectName("gridLayout")

        self.cbx_paths.setObjectName("cbx_paths")
        self.cbx_chooser.setObjectName("cbx_chooser")
        self.main_layout.addWidget(self.cbx_paths, 0, 1, 1, 1)
        self.main_layout.addWidget(self.cbx_chooser, 0, 0, 1, 1)
        self.cbx_chooser.sync_widget(global_variables.json_paths)
        self.cbx_chooser.currentIndexChanged.connect(self.cbx_chooser_current_changed)
        self.cbx_paths.currentIndexChanged.connect(self.cbx_paths_current_changed)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cbx_chooser.sizePolicy().hasHeightForWidth())
        self.cbx_chooser.setSizePolicy(size_policy)

        self.tabw_main.setObjectName("tabWidget")
        self.main_layout.addWidget(self.tabw_main, 1, 0, 1, 2)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def cbx_chooser_current_changed(self):
        gzis_funcs.sync_cbx_path(self.cbx_chooser)
        self.cbx_paths.sync_widget(global_variables.json_files)

    def cbx_paths_current_changed(self):
        path = f"{global_variables.current_path}/{self.cbx_paths.currentText()}.json"
        print(path)