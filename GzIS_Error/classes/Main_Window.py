from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTabBar, QVBoxLayout, QSizePolicy, QHBoxLayout
from PyQt5 import QtCore, QtWidgets
from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.classes import ComboBox, TabWidget


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget()
        self.menubar = QtWidgets.QMenuBar()
        self.statusbar = QtWidgets.QStatusBar()
        self.main_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.cbx_jsons = ComboBox.MyComboBox()
        self.cbx_ar_pos = ComboBox.MyComboBox()
        self.vertical_lay = QVBoxLayout()
        self.tbar_headers = QTabBar()
        self.horiontallay = QHBoxLayout()
       # self.horiontallay.addWidget()
        self.tabw_main = QTabBar()
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

        self.cbx_jsons.setObjectName("cbx_paths")
        self.cbx_ar_pos.setObjectName("cbx_chooser")
        self.main_layout.addWidget(self.cbx_ar_pos, 0, 0, Qt.AlignTop)
        self.main_layout.addWidget(self.cbx_jsons, 0, 1, Qt.AlignTop)

        self.cbx_ar_pos.sync_widget(global_variables.json_paths)
        self.cbx_ar_pos.currentIndexChanged.connect(self.cbx_arpos_current_changed)
        self.cbx_jsons.currentIndexChanged.connect(self.cbx_paths_current_changed)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cbx_ar_pos.sizePolicy().hasHeightForWidth())
        self.cbx_ar_pos.setSizePolicy(size_policy)

        # self.tabw_main.setObjectName("tabWidget")
        # self.main_layout.addWidget(self.tabw_main, 1, 0, 1, 2)
        self.tbar_headers.setObjectName("tabbar_headers")
        self.tbar_headers.addTab("yaskaaa")
        # pol = QSizePolicy()
        # self.tbar_headers.setSizePolicy()
        with open("UIs/GzIS_tabwid_styel_sheet.css", "r") as twsheet:
            self.tbar_headers.setStyleSheet(str(twsheet.read()))

        self.tbar_headers.setGeometry(-500, -500, 640, 480)
        self.tbar_headers.move(-50, -50)
        print(self.tbar_headers.geometry())
        self.main_layout.addWidget(self.tbar_headers, 1, 0, Qt.AlignTop)


        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def cbx_arpos_current_changed(self):
        self.cbx_jsons.blockSignals(True)

        # while self.tabw_main.count() > 0:
        #     self.tabw_main.removeTab(0)

        gzis_funcs.sync_cbx_path(self.cbx_ar_pos)
        self.cbx_jsons.sync_widget(global_variables.json_files)

    def cbx_paths_current_changed(self):

        if self.cbx_jsons.currentIndex() != -1:
            global_variables.current_path += f"/{self.cbx_ar_pos.currentText()}/{self.cbx_jsons.currentText()}"

#            gzis_funcs.set_tabwid(global_variables.current_path, self.tabw_main)
        self.cbx_jsons.blockSignals(True)

