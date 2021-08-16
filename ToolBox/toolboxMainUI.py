from PyQt5 import QtCore, QtWidgets


class UIMainWindow(object):
    def setup_ui(self, main_window):
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.horizontal_lay = QtWidgets.QHBoxLayout(self.centralwidget)
        main_window.setCentralWidget(self.centralwidget)
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
