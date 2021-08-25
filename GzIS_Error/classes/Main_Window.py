from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QMenuBar, QStatusBar, QGridLayout, \
    QSizePolicy, QTableWidget
from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.classes import ComboBox, Tabbar


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName("MainWindow")
        self.centralwidget = QWidget()
        self.menubar = QMenuBar()
        self.statusbar = QStatusBar()
        self.main_layout = QGridLayout(self.centralwidget)

        self.cbx_jsons = ComboBox.MyComboBox()
        self.cbx_ar_pos = ComboBox.MyComboBox()

        self.cbx_lay = QHBoxLayout()
        self.cbx_lay.addWidget(self.cbx_ar_pos)
        self.cbx_lay.addWidget(self.cbx_jsons)

        self.tbar_headers = Tabbar.MyTabBar()
        self.table_content = QTableWidget()
        self.table_content.setColumnCount(4)
        self.table_content.setRowCount(3)

        self.lay_content = QVBoxLayout()
        self.lay_content.addWidget(self.tbar_headers)
        self.lay_content.addWidget(self.table_content)

        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(QSize(800, 500))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.main_layout.setObjectName("gridLayout")

        self.cbx_jsons.setObjectName("cbx_paths")
        self.cbx_ar_pos.setObjectName("cbx_chooser")

        self.cbx_ar_pos.sync_widget(global_variables.json_paths)
        self.cbx_ar_pos.currentIndexChanged.connect(self.cbx_arpos_current_changed)
        self.cbx_jsons.currentIndexChanged.connect(self.cbx_paths_current_changed)
        self.cbx_jsons.blockSignals(True)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cbx_ar_pos.sizePolicy().hasHeightForWidth())
        self.cbx_ar_pos.setSizePolicy(size_policy)

        self.tbar_headers.setObjectName("tabbar_headers")

        self.main_layout.addLayout(self.cbx_lay, 0, 0)
        self.main_layout.addLayout(self.lay_content, 1, 0, Qt.AlignTop)

        self.retranslate_ui()
        QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def cbx_arpos_current_changed(self):
        self.cbx_jsons.blockSignals(True)
        self.clear_contents()

        gzis_funcs.sync_global_jsonfiles(self.cbx_ar_pos)
        self.cbx_jsons.sync_widget(global_variables.json_files)

    def cbx_paths_current_changed(self):
        if self.cbx_jsons.currentIndex() != -1:
            global_variables.current_path += f"/{self.cbx_ar_pos.currentText()}/{self.cbx_jsons.currentText()}"
            self.statusbar.showMessage(global_variables.current_path)

            gzis_funcs.set_tabbar(global_variables.current_path, self.tbar_headers, self.table_content)

    def clear_contents(self):
        while self.table_content.columnCount() > 0:
            self.table_content.removeColumn(0)
        while self.table_content.rowCount() > 0:
            self.table_content.removeRow(0)
        while self.tbar_headers.count() > 0:
            self.tbar_headers.removeTab(0)