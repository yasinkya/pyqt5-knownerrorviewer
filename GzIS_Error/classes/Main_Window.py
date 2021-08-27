from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QMenuBar, QStatusBar, QGridLayout, \
    QSizePolicy, QTableWidget, QMenu, QAction
from pyqt5_plugins.examplebutton import QtWidgets
from pyqt5_plugins.examples.exampleqmlitem import QtCore

from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.classes import ComboBox, TabBar, table_widget


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName("MainWindow")
        self.centralwidget = QWidget()
        self.main_layout = QGridLayout(self.centralwidget)
        self.statusbar = QStatusBar()

        self.menubar = QMenuBar(self)
        self.menu_filter = QMenu(self.menubar)
        self.menu_find = QMenu(self.menubar)

        self.filter_isaccept = QMenu(self.menu_filter)
        self.filter_link = QMenu(self.menu_filter)
        self.find_byname = QMenu(self.menu_find)
        self.find_bytests = QMenu(self.menu_find)

        self.action_true = QAction(self)
        self.action_false = QAction(self)
        self.action_none = QAction(self)
        self.action_exist = QAction(self)
        self.action_exist.triggered.connect(self.action_true_cliced)

        self.action_byname = QAction(self)
        self.action_bytests = QAction(self)



        self.cbx_jsons = ComboBox.MyComboBox()
        self.cbx_ar_pos = ComboBox.MyComboBox()

        self.cbx_lay = QHBoxLayout()
        self.cbx_lay.addWidget(self.cbx_ar_pos)
        self.cbx_lay.addWidget(self.cbx_jsons)

        self.tbar_headers = TabBar.CreateTabbar()
        self.table_content = QTableWidget()

        self.lay_content = QVBoxLayout()
        self.lay_content.addWidget(self.tbar_headers)
        self.lay_content.addWidget(self.table_content)

        self.tbar_headers.currentChanged.connect(self.tbar_changed_triger)

        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(QSize(1000, 500))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.main_layout.setObjectName("gridLayout")

        self.filter_isaccept.setObjectName("Is Accept")
        self.filter_isaccept.addAction(self.action_true)
        self.action_true.changed.connect(self.action_true_cliced)
        self.filter_isaccept.addAction(self.action_false)
        self.filter_link.setObjectName("Link")
        self.filter_link.addAction(self.action_exist)
        self.filter_link.addAction(self.action_none)

        self.find_byname.setObjectName("byname")
        self.find_bytests.setObjectName("by tests")
        self.find_byname.addAction(self.action_byname)
        self.find_bytests.addAction(self.action_bytests)

        self.menu_filter.addAction(self.filter_link.menuAction())
        self.menu_filter.addAction(self.filter_isaccept.menuAction())

        self.menu_find.addAction(self.find_byname.menuAction())
        self.menu_find.addAction(self.find_bytests.menuAction())

        self.menubar.addAction(self.menu_find.menuAction())
        self.menubar.addAction(self.menu_filter.menuAction())

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

        self.menu_filter.setTitle(_translate("MainWindow", "Filter"))
        self.menu_find.setTitle(_translate("MainWindow", "Find"))
        self.filter_isaccept.setTitle(_translate("MainWindow", "Is Accept"))
        self.filter_link.setTitle(_translate("MainWindow", "Link"))
        self.find_byname.setTitle(_translate("MainWindow", "By Name"))
        self.find_bytests.setTitle(_translate("MainWindow", "By Test"))

        self.action_true.setText(_translate("MainWindow", "True"))
        self.action_false.setText(_translate("MainWindow", "False"))

        self.action_none.setText(_translate("MainWindow", "None"))
        self.action_exist.setText(_translate("MainWindow", "Exist"))

        self.action_byname.setText(_translate("MainWindow", "Byname"))
        self.action_bytests.setText(_translate("MainWindow", "By Tests"))


    def cbx_arpos_current_changed(self):
        self.cbx_jsons.blockSignals(True)
        self.clear_contents()
        self.tbar_headers.blockSignals(False)
        gzis_funcs.sync_global_jsonfiles(self.cbx_ar_pos)
        self.cbx_jsons.sync_widget(global_variables.json_files)

    def cbx_paths_current_changed(self):
        if self.cbx_jsons.currentIndex() != -1:
            global_variables.current_path += f"/{self.cbx_ar_pos.currentText()}/{self.cbx_jsons.currentText()}"
            self.statusbar.showMessage(global_variables.current_path)

            gzis_funcs.set_tabbar(global_variables.current_path, self.tbar_headers)

    def clear_contents(self):
        self.table_content.clear()
        self.table_content.setColumnCount(0)
        self.table_content.setRowCount(0)
        self.tbar_headers.blockSignals(True)
        while self.tbar_headers.count() > 0:
            self.tbar_headers.removeTab(0)

    def tbar_changed_triger(self, idx):
        data = global_variables.current_jsondata[self.tbar_headers.tabText(idx)]["tests"]
        table_widget.init_widget(self.table_content, data)

    def action_true_cliced(self):
        print("heloooo")
