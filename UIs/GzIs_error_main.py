# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GzIs_error_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_cbxes = QtWidgets.QHBoxLayout()
        self.layout_cbxes.setObjectName("layout_cbxes")
        self.cbx_ar_pos = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_ar_pos.sizePolicy().hasHeightForWidth())
        self.cbx_ar_pos.setSizePolicy(sizePolicy)
        self.cbx_ar_pos.setStyleSheet("")
        self.cbx_ar_pos.setObjectName("cbx_ar_pos")
        self.layout_cbxes.addWidget(self.cbx_ar_pos)
        self.cbx_jsons = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_jsons.setObjectName("cbx_jsons")
        self.layout_cbxes.addWidget(self.cbx_jsons)
        self.gridLayout.addLayout(self.layout_cbxes, 0, 1, 1, 1)
        self.layout_content = QtWidgets.QVBoxLayout()
        self.layout_content.setObjectName("layout_content")
        self.table_content = QtWidgets.QTableWidget(self.centralwidget)
        self.table_content.setObjectName("table_content")
        self.table_content.setColumnCount(0)
        self.table_content.setRowCount(0)
        self.layout_content.addWidget(self.table_content)
        self.gridLayout.addLayout(self.layout_content, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
