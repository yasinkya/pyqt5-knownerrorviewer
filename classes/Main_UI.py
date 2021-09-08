from PyQt5.QtCore import Qt, QObject, QEvent, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QToolButton
from classes.Main_Window import Window


class MainWindow(Window):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(700, 500)
        self.btn_close = QToolButton()
        self.curpos = QPoint()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)

    def setupUi(self, MainWindow):
        super().setupUi(self)
        print("custom tilebar")

        # Custom tilebar actions - close
        self.btn_close.setText("x")
        self.btn_close.setStyleSheet("QToolButton{ background-color: rgb(45,45,40); color: #fffff0; font-size: 15px;"
                                     "min-width: 1.6em; max-height: 1.5em;"
                                     "}")
        self.btn_close.clicked.connect(self.close)
        self.menubar.setStyleSheet("QMenuBar{background-color: rgb(145,45,45); color: #fffff0}"
                                          "QMenu{background-color: rgb(70,70,70);}")
        self.menubar.setCornerWidget(self.btn_close)

    def eventFilter(self, obj: QObject, _event: QMouseEvent):
        if _event.type() == QEvent.MouseButtonPress:
            self.curpos = _event.pos()

        if _event.type() == QEvent.MouseMove:
            if _event.buttons() & Qt.LeftButton:
                offset = _event.pos()
                self.move(self.pos() + offset - self.curpos)
        return super().eventFilter(obj, _event)
