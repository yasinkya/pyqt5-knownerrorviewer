from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication, QRect
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QStatusBar, QGridLayout, \
    QSizePolicy, QTableWidget, QPushButton, QComboBox, QLabel, QCheckBox, QMenuBar, QMenu, QToolButton
from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.classes import ComboBox, TabBar, table_widget_tests, table_widget_target
from PIL import Image
from GzIS_Error.UIs import GzIs_error_main

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        main_ui = GzIs_error_main.UiMainWindow()
        main_ui.setup_ui(self)
        self.tbar_headers = main_ui.tbar_headers
        self.cbx_ar_pos = main_ui.cbx_ar_pos
        self.cbx_jsons = main_ui.cbx_jsons
        self.tbar_headers.currentChanged.connect(self.tbar_changed_trigger)
        self.cbx_ar_pos.currentIndexChanged.connect(self.cbx_arpos_current_changed)


    #     self.setObjectName("MainWindow")
    #     # todo: custom mainwindow tilebar
    #     # self.setWindowFlag(Qt.FramelessWindowHint)
    #
    #     # Mainwindow Window icon
    #     fname = r'icons/raptiye.png'
    #     self.raptiye = Image.open(fname)
    #     self.raptiye.save('icons/raptiye.ico', format='ICO', sizes=[(32, 32)])
    #     self.setWindowIcon(QIcon('icons/raptiye.ico'))
    #
    #     # mainwidget and layout
    #     self.centralwidget = QWidget()
    #     self.main_layout = QGridLayout(self.centralwidget)
    #
    #     # Status Bar for show current json path and some actions
    #     self.statusbar = QStatusBar()
    #
    #     # Change Main window's palette with button at statusbar
    #     icon = QtGui.QIcon()
    #     icon.addPixmap(QPixmap('icons/palette.png'))
    #     self.btn_palette = QPushButton()
    #     self.btn_palette.setIcon(QIcon('icons/palette.png'))
    #     self.btn_palette.clicked.connect(self.btn_palette_trigger)
    #
    #     # when check_exception was clicked show other json (target.json)
    #     self.check_exception = QCheckBox()
    #     self.check_exception.setText("Exception Test Suites: ")
    #     self.check_exception.setLayoutDirection(Qt.RightToLeft)
    #     self.check_exception.clicked.connect(self.check_target_trigger)
    #
    #     # filter combobox using as tests' is accept value
    #     self.lbl_isaccept = QLabel()
    #     self.cbx_isaccept = QComboBox()
    #     self.lbl_isaccept.setText("Is Accept :")
    #     self.cbx_isaccept.addItems(["All", "True", "False"])
    #     # connect event - if is cbxisaccpet current text == false (or true)
    #     # remove items which item's accept value of isaccept  is True (for isaccpet= false)
    #     self.cbx_isaccept.currentIndexChanged.connect(lambda: gzis_funcs.isaccepted_filter(
    #         self.table_content, self.cbx_isaccept.currentText()))
    #
    #     # add widgets to status bar
    #     self.statusbar.addPermanentWidget(self.check_exception, 0)
    #     self.statusbar.addPermanentWidget(self.btn_palette, 0)
    #
    #     # select test as arinc or posix then select the any json file
    #     self.cbx_ar_pos = ComboBox.MyComboBox()
    #     self.cbx_jsons = ComboBox.MyComboBox()
    #
    #     self.layout_cbxes = QHBoxLayout()
    #     self.layout_cbxes.addWidget(self.cbx_ar_pos)
    #     self.layout_cbxes.addWidget(self.cbx_jsons)
    #
    #     # then select a tab created dynamicly, its will create table dynamicly
    #     self.table_content = QTableWidget()
    #     self.tbar_headers = TabBar.CreateTabbar()
    #     self.tbar_headers.currentChanged.connect(self.tbar_changed_trigger)
    #
    #     # this layout at main grid layout add tbar and tablewidget
    #     self.layout_content = QVBoxLayout()
    #     self.layout_content.addWidget(self.tbar_headers)
    #     self.layout_content.addWidget(self.table_content)
    #
    #     self.set_items_stylesheets()
    #     self.setup_ui()
    #
    # def setup_ui(self):
    #     self.cbx_jsons.setObjectName("cbx_paths")
    #     self.statusbar.setObjectName("statusbar")
    #     self.cbx_ar_pos.setObjectName("cbx_chooser")
    #     self.main_layout.setObjectName("gridLayout")
    #     self.tbar_headers.setObjectName("tabbar_headers")
    #     self.centralwidget.setObjectName("centralwidget")
    #
    #     self.setStatusBar(self.statusbar)
    #     self.setMinimumSize(QSize(1000, 500))
    #     self.setCentralWidget(self.centralwidget)
    #
    #     self.cbx_ar_pos.currentIndexChanged.connect(self.cbx_arpos_current_changed)
    #     self.cbx_jsons.currentIndexChanged.connect(self.cbx_paths_current_changed)
    #     self.cbx_ar_pos.sync_widget(global_variables.json_paths)
    #     self.cbx_jsons.blockSignals(False)
    #
    #     size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    #     size_policy.setHeightForWidth(self.cbx_ar_pos.sizePolicy().hasHeightForWidth())
    #     size_policy.setHorizontalStretch(0)
    #     size_policy.setVerticalStretch(0)
    #     self.cbx_ar_pos.setSizePolicy(size_policy)
    #
    #     self.menubar = QMenuBar(self)
    #     self.menubar.setObjectName("menubar")
    #     self.setMenuBar(self.menubar)
    #     self.menu = QMenu()
    #     self.menu.setTitle("kak")
    #     self.menu.addAction("kek")
    #     self.menu.setObjectName("menu")
    #     self.menubar.addAction(self.menu.menuAction())
    #     x_btn = QToolButton()
    #     x_btn.setText("X")
    #     x_btn.clicked.connect(self.close)
    #     self.menuBar().setCornerWidget(x_btn)
    #
    #     self.main_layout.addLayout(self.layout_cbxes, 0, 0)
    #     self.main_layout.addLayout(self.layout_content, 1, 0, Qt.AlignTop)
    #
    #     self.retranslate_ui()
    #
    # def retranslate_ui(self):
    #     _translate = QCoreApplication.translate
    #     self.setWindowTitle(_translate("GzIS Error", "GzIS Error"))
    #
    def cbx_arpos_current_changed(self):
        # self.clear_contents()
        self.tbar_headers.blockSignals(False)
        gzis_funcs.sync_global_jsonfiles(self.cbx_ar_pos)
        self.cbx_jsons.sync_widget(global_variables.json_files)

    def cbx_paths_current_changed(self):
        if self.cbx_jsons.currentIndex() != -1:
            self.statusbar.addPermanentWidget(self.lbl_isaccept, 0)
            self.statusbar.addPermanentWidget(self.cbx_isaccept, 0)
            self.statusbar.showMessage(global_variables.current_path)
            self.clear_contents()
            self.tbar_headers.blockSignals(False)

            gzis_funcs.set_tabbar(f"{global_variables.folder}/{self.cbx_ar_pos.currentText()}/"
                                  f"{self.cbx_jsons.currentText()}", self.tbar_headers, False)

    def clear_contents(self):
        self.table_content.clear()
        self.table_content.setColumnCount(0)
        self.table_content.setRowCount(0)
        self.tbar_headers.blockSignals(True)
        while self.tbar_headers.count() > 0:
            self.tbar_headers.removeTab(0)

    def tbar_changed_trigger(self, idx):
        json_data = global_variables.current_jsondata[self.tbar_headers.tabText(idx)]
        # for test suites
        if not self.check_exception.isChecked():
            table_widget_tests.init_widget(self.table_content, json_data["tests"])
        # for target
        else:
            table_widget_target.init_widget(self.table_content, json_data)

    def btn_palette_trigger(self):
        palette = QPalette()
        if global_variables.is_light:
            palette.setBrush(self.backgroundRole(), QColor(45, 45, 45))
            global_variables.is_light = False
        else:
            palette.setBrush(self.backgroundRole(), QColor(220, 220, 220))
            global_variables.is_light = True
        self.setPalette(palette)

    def check_target_trigger(self):
        self.clear_contents()
        if self.check_exception.isChecked():
            self.set_cbx_enabled(False)
            self.set_table_header_visible(False)
            path = r"knownError\target.json"
            gzis_funcs.set_tabbar(path, self.tbar_headers, True)
            self.tbar_headers.blockSignals(False)
            table_widget_target.init_widget(self.table_content,
                                            global_variables.current_jsondata[self.tbar_headers.tabText(0)])
        else:
            self.set_cbx_enabled(True)
            self.set_table_header_visible(True)
            self.cbx_ar_pos.setCurrentIndex(-1)

    def set_cbx_enabled(self, val: bool):
        self.cbx_jsons.setEnabled(val)
        self.cbx_ar_pos.setEnabled(val)

    def set_table_header_visible(self, val: bool):
        self.table_content.verticalHeader().setVisible(val)
        self.table_content.horizontalHeader().setVisible(val)
    #
    # def set_items_stylesheets(self):
    #     self.statusbar.setStyleSheet("QStatusBar{"
    #                                  "padding-left:8px;background: rgb(45,45,45);"
    #                                  "color:#fffff0;font-weight;}")
    #     self.btn_palette.setStyleSheet("QPushButton{background-color: rgb(45 ,45, 45); margin-right: 10px; }")
    #     self.check_exception.setStyleSheet("QCheckBox{color: #fffff0; margin-right: 10px; margin-left: 10px;}")
    #     self.lbl_isaccept.setStyleSheet("QLabel{color: #fffff0; margin-left: 10px}")
    #     with open("UIs/GzIs_cbx_style_sheet.css", "r") as cbxsheet:
    #         self.cbx_isaccept.setStyleSheet(str(cbxsheet.read()))
