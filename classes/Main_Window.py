from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QPushButton, QCheckBox, QLabel, QComboBox
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
import global_variables, gzis_funcs
from classes import table_widget_tests, table_widget_target, TabBar
from UIs.GzIs_error_main import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.btn_palette = QPushButton()
        self.check_exception = QCheckBox()
        self.lbl_isaccept = QLabel()
        self.cbx_isaccept = QComboBox()

        self.tbar_headers = TabBar.CreateTabbar()

        self.setupUi(self)
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # self.layout_content.addWidget(self.tbar_headers)
        self.setup_widget()
        self.init_comboboxes()
        self.init_statusbar()
    def setup_widget(self):
        # self.btn_palette.clicked.connect(self.btn_palette_trigger)
        # self.check_exception.clicked.connect(self.check_target_trigger)
        # self.tbar_headers.currentChanged.connect(self.tbar_changed_trigger)
        self.cbx_ar_pos.currentIndexChanged.connect(self.cbx_arpos_current_changed)
        self.cbx_jsons.currentIndexChanged.connect(self.cbx_paths_current_changed)
        self.cbx_ar_pos.setCurrentIndex(1)

    def cbx_arpos_current_changed(self):
        self.clear_contents()
        self.tbar_headers.blockSignals(False)
        gzis_funcs.sync_global_jsonfiles(self.cbx_ar_pos)
        self.cbx_jsons.clear()
        self.cbx_jsons.addItems(global_variables.json_files)

    def cbx_paths_current_changed(self):
        if self.cbx_jsons.currentIndex() != -1:
            self.clear_contents()
            self.statusbar.addPermanentWidget(self.lbl_isaccept, 0)
            self.statusbar.addPermanentWidget(self.cbx_isaccept, 0)
            self.statusbar.showMessage(global_variables.current_path)
            self.tbar_headers.blockSignals(False)

            gzis_funcs.set_tabbar(f"{global_variables.folder}/{self.cbx_ar_pos.currentText()}/"
                                  f"{self.cbx_jsons.currentText()}", self.tbar_headers, False)

    def clear_contents(self):
        self.table_content.clear()
        self.table_content.setRowCount(0)
        self.table_content.setColumnCount(0)
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
            palette.setBrush(self.backgroundRole(), QColor(30, 30, 30))
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
            self.cbx_ar_pos.setCurrentIndex(0)

    def set_cbx_enabled(self, val: bool):
        self.cbx_jsons.setEnabled(val)
        self.cbx_ar_pos.setEnabled(val)

    def set_table_header_visible(self, val: bool):
        self.table_content.verticalHeader().setVisible(val)
        self.table_content.horizontalHeader().setVisible(val)

# ------------------------------------------------------------------
    def init_comboboxes(self):
        self.cbx_jsons.setObjectName("cbx_paths")
        self.statusbar.setObjectName("statusbar")
        self.cbx_ar_pos.setObjectName("cbx_chooser")

        # self.tbar_headers.setObjectName("tabbar_headers")
        self.centralwidget.setObjectName("centralwidget")

        # with open("UIs/GzIs_cbx_style_sheet.css", "r") as cbxsheet:
        #     self.cbx_isaccept.setStyleSheet(str(cbxsheet.read()))

        self.cbx_ar_pos.addItems(global_variables.json_paths)
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
        # self.btn_palette.setStyleSheet("QPushButton{background-color: rgb(45 ,45, 45); margin-right: 10px; }")
        # self.check_exception.setStyleSheet("QCheckBox{color: #fffff0; margin-right: 10px; margin-left: 10px;}")
        # self.lbl_isaccept.setStyleSheet("QLabel{color: #fffff0; margin-left: 10px}")
        # Change Main window's palette with button at statusbar
        icon = QtGui.QIcon()
        icon.addPixmap(QPixmap('icons/palette.png'))
        # self.btn_palette.setIcon(QIcon('icons/palette.png'))

        # when check_exception was clicked show other json (target.json)
        # self.check_exception.setText("Exception Test Suites: ")
        # self.check_exception.setLayoutDirection(Qt.RightToLeft)

        # filter combobox using as tests' is accept value
        # self.lbl_isaccept.setText("Is Accept :")
        # self.cbx_isaccept.addItems(["All", "True", "False"])
        # connect event - if is cbxisaccpet current text == false (or true)
        # remove items which item's accept value of isaccept  is True (for isaccpet= false)
        # self.cbx_isaccept.currentIndexChanged.connect(lambda: gzis_funcs.isaccepted_filter(
        #     self.table_content, self.cbx_isaccept.currentText()))
        #
        # # add widgets to status bar
        # self.statusbar.addPermanentWidget(self.check_exception, 0)
        # self.statusbar.addPermanentWidget(self.btn_palette, 0)