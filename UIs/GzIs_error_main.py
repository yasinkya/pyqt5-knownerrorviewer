from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QCoreApplication, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QStatusBar, QPushButton, QCheckBox, QLabel, QComboBox, QHBoxLayout, \
    QTableWidget, QVBoxLayout, QSizePolicy, QMenuBar, QMenu, QToolButton

import gzis_funcs, global_variables
from classes import ComboBox, TabBar


class UiMainWindow(object):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.centralwidget = QWidget()
        self.statusbar = QStatusBar()
        self.btn_palette = QPushButton()
        self.check_exception = QCheckBox()
        self.lbl_isaccept = QLabel()
        self.cbx_isaccept = QComboBox()
        self.cbx_ar_pos = ComboBox.MyComboBox()
        self.cbx_jsons = ComboBox.MyComboBox()
        self.layout_cbxes = QHBoxLayout()
        self.table_content = QTableWidget()
        self.tbar_headers = TabBar.CreateTabbar()
        self.layout_content = QVBoxLayout()
        self.menubar = QMenuBar()
        self.menu = QMenu()
        # self.x_btn = QToolButton()
        self.main_layout = QGridLayout(self.centralwidget)

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.setMinimumSize(QSize(1000, 500))
        main_window.setMenuBar(self.menubar)
        main_window.setStatusBar(self.statusbar)
        main_window.setCentralWidget(self.centralwidget)

        # self.x_btn.clicked.connect(main_window.close)
        # main_window.menuBar().setCornerWidget(self.x_btn)

        # Mainwindow Window icon
        fname = r'icons/raptiye.png'
        raptiye = Image.open(fname)
        raptiye.save('icons/raptiye.ico', format='ICO', sizes=[(32, 32)])
        main_window.setWindowIcon(QIcon('icons/raptiye.ico'))

        # select test as arinc or posix then select the any json file
        self.layout_cbxes.addWidget(self.cbx_ar_pos)
        self.layout_cbxes.addWidget(self.cbx_jsons)

        # this layout at main grid layout add tbar and tablewidget
        self.layout_content.addWidget(self.tbar_headers)
        self.layout_content.addWidget(self.table_content)

        # then select a tab created dynamicly, its will create table dynamicly

        self.main_layout.addLayout(self.layout_cbxes, 0, 0)
        self.main_layout.addLayout(self.layout_content, 1, 0, Qt.AlignTop)

        self.retranslate_ui(main_window)

        self.init_statusbar()
        self.init_comboboxes()

        # main_window.setWindowFlag(Qt.FramelessWindowHint)
        # self.init_custom_tilebar()

    @staticmethod
    def retranslate_ui(main_window):
        _translate = QCoreApplication.translate
        main_window.setWindowTitle(_translate("GzIS Error", "GzIS Error"))

    def init_comboboxes(self):
        self.cbx_jsons.setObjectName("cbx_paths")
        self.statusbar.setObjectName("statusbar")
        self.cbx_ar_pos.setObjectName("cbx_chooser")
        self.main_layout.setObjectName("gridLayout")
        self.tbar_headers.setObjectName("tabbar_headers")
        self.centralwidget.setObjectName("centralwidget")

        with open("UIs/GzIs_cbx_style_sheet.css", "r") as cbxsheet:
            self.cbx_isaccept.setStyleSheet(str(cbxsheet.read()))

        self.cbx_ar_pos.sync_widget(global_variables.json_paths)
        self.cbx_jsons.blockSignals(False)

        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHeightForWidth(self.cbx_ar_pos.sizePolicy().hasHeightForWidth())
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        self.cbx_ar_pos.setSizePolicy(size_policy)

    def init_statusbar(self):
        self.statusbar.setStyleSheet("QStatusBar{"
                                     "padding-left:8px;background: rgb(45,45,45);"
                                     "color:#fffff0;font-weight;}")
        self.btn_palette.setStyleSheet("QPushButton{background-color: rgb(45 ,45, 45); margin-right: 10px; }")
        self.check_exception.setStyleSheet("QCheckBox{color: #fffff0; margin-right: 10px; margin-left: 10px;}")
        self.lbl_isaccept.setStyleSheet("QLabel{color: #fffff0; margin-left: 10px}")
        # Change Main window's palette with button at statusbar
        icon = QtGui.QIcon()
        icon.addPixmap(QPixmap('icons/palette.png'))
        self.btn_palette.setIcon(QIcon('icons/palette.png'))

        # when check_exception was clicked show other json (target.json)
        self.check_exception.setText("Exception Test Suites: ")
        self.check_exception.setLayoutDirection(Qt.RightToLeft)

        # filter combobox using as tests' is accept value
        self.lbl_isaccept.setText("Is Accept :")
        self.cbx_isaccept.addItems(["All", "True", "False"])
        # connect event - if is cbxisaccpet current text == false (or true)
        # remove items which item's accept value of isaccept  is True (for isaccpet= false)
        self.cbx_isaccept.currentIndexChanged.connect(lambda: gzis_funcs.isaccepted_filter(
            self.table_content, self.cbx_isaccept.currentText()))

        # add widgets to status bar
        self.statusbar.addPermanentWidget(self.check_exception, 0)
        self.statusbar.addPermanentWidget(self.btn_palette, 0)

    def init_custom_tilebar(self):
        self.menubar.setObjectName("menubar")
        self.menu.setTitle("kak")
        self.menu.addAction("kek")
        self.menu.setObjectName("menu")
        self.menubar.addAction(self.menu.menuAction())
        self.x_btn.setText("X")
