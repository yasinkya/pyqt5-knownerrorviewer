from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QMenuBar, QStatusBar, QGridLayout, \
    QSizePolicy, QTableWidget, QMenu
from pyqt5_plugins.examplebutton import QtWidgets
from pyqt5_plugins.examples.exampleqmlitem import QtCore

from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.classes import ComboBox, TabBar, table_widget


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setObjectName("MainWindow")
        self.setStyleSheet("QWidget{background-color: #fffafa;}")
        self.centralwidget = QWidget()
        self.menubar = QMenuBar(self)
        self.statusbar = QStatusBar()
        self.main_layout = QGridLayout(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 24))
        self.menubar.setObjectName("menubar")
        self.menufilter = QtWidgets.QMenu(self.menubar)
        self.menufilter.setObjectName("menufilter")
        self.menuby_isaccept = QtWidgets.QMenu(self.menufilter)
        self.menuby_isaccept.setObjectName("menuby_isaccept")
        self.menuby_link = QtWidgets.QMenu(self.menufilter)
        self.menuby_link.setObjectName("menuby_link")
        self.menufind = QtWidgets.QMenu(self.menubar)
        self.menufind.setObjectName("menufind")

        self.actiontrue = QtWidgets.QAction()
        self.actiontrue.setObjectName("actiontrue")
        self.actionfalse = QtWidgets.QAction()
        self.actionfalse.setObjectName("actionfalse")
        self.actionNone = QtWidgets.QAction()
        self.actionNone.setObjectName("actionNone")
        self.actionnon_Exist = QtWidgets.QAction()
        self.actionnon_Exist.setObjectName("actionnon_Exist")
        self.actionby_name = QtWidgets.QAction()
        self.actionby_name.setObjectName("actionby_name")
        self.actionby_tests = QtWidgets.QAction()
        self.actionby_tests.setObjectName("actionby_tests")
        self.menuby_isaccept.addSeparator()
        self.menuby_isaccept.addAction(self.actiontrue)
        self.menuby_isaccept.addAction(self.actionfalse)
        self.menuby_link.addAction(self.actionNone)
        self.menuby_link.addAction(self.actionnon_Exist)
        self.menufilter.addAction(self.menuby_isaccept.menuAction())
        self.menufilter.addAction(self.menuby_link.menuAction())
        self.menufind.addAction(self.actionby_name)
        self.menufind.addAction(self.actionby_tests)
        self.menubar.addAction(self.menufilter.menuAction())
        self.menubar.addAction(self.menufind.menuAction())



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

        self.menufilter.setTitle(_translate("MainWindow", "filter"))
        self.menuby_isaccept.setTitle(_translate("MainWindow", "by isaccept"))
        self.menuby_link.setTitle(_translate("MainWindow", "by link"))
        self.menufind.setTitle(_translate("MainWindow", "find"))
        self.actiontrue.setText(_translate("MainWindow", "true"))
        self.actionfalse.setText(_translate("MainWindow", "false"))
        self.actionNone.setText(_translate("MainWindow", "Exist"))
        self.actionnon_Exist.setText(_translate("MainWindow", "non Exist"))
        self.actionby_name.setText(_translate("MainWindow", "by name"))
        self.actionby_tests.setText(_translate("MainWindow", "by tests"))

        

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
