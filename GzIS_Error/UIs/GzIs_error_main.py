from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QStatusBar, QPushButton, QCheckBox, QLabel, QComboBox, QHBoxLayout, \
    QTableWidget, QVBoxLayout

from GzIS_Error import gzis_funcs
from GzIS_Error.classes import ComboBox, TabBar


class UiMainWindow(object):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.centralwidget = QWidget()
        self.main_layout = QGridLayout(self.centralwidget)
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

    def setup_ui(self, main_window):

        main_window.setObjectName("MainWindow")
        # todo: custom mainwindow tilebar
        # self.setWindowFlag(Qt.FramelessWindowHint)

        # Mainwindow Window icon
        fname = r'icons/raptiye.png'
        raptiye = Image.open(fname)
        raptiye.save('icons/raptiye.ico', format='ICO', sizes=[(32, 32)])
        main_window.setWindowIcon(QIcon('icons/raptiye.ico'))

        # Change Main window's palette with button at statusbar
        icon = QtGui.QIcon()
        icon.addPixmap(QPixmap('icons/palette.png'))
        self.btn_palette.setIcon(QIcon('icons/palette.png'))
        # self.btn_palette.clicked.connect(self.btn_palette_trigger)

        # when check_exception was clicked show other json (target.json)
        self.check_exception.setText("Exception Test Suites: ")
        self.check_exception.setLayoutDirection(Qt.RightToLeft)
        # self.check_exception.clicked.connect(self.check_target_trigger)

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

        # select test as arinc or posix then select the any json file
        self.layout_cbxes.addWidget(self.cbx_ar_pos)
        self.layout_cbxes.addWidget(self.cbx_jsons)

        # then select a tab created dynamicly, its will create table dynamicly
        # self.tbar_headers.currentChanged.connect(self.tbar_changed_trigger)

        # this layout at main grid layout add tbar and tablewidget
        self.layout_content.addWidget(self.tbar_headers)
        self.layout_content.addWidget(self.table_content)

        # self.set_items_stylesheets()

    @staticmethod
    def retranslate_ui(main_window):
        _translate = QCoreApplication.translate
        main_window.setWindowTitle(_translate("GzIS Error", "GzIS Error"))

