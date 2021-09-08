from typing import Union
from PyQt5.QtCore import Qt, QObject, QEvent, QPoint
from PyQt5.QtGui import QMouseEvent, QIcon
from PyQt5.QtWidgets import QToolButton, QMenuBar, QMenu, QAction
from classes.Main_Window import Window


class MainWindow(Window):
    act_close: Union[QAction, QAction]
    menu_filter: Union[QMenu, QMenu]
    menu_icon: Union[QMenu, QMenu]
    left_menubar: Union[QMenuBar, QMenuBar]
    right_menubar: Union[QMenuBar, QMenuBar]

    def __init__(self):
        super(Window, self).__init__()
        self.btn_close = QToolButton()
        self.curpos = QPoint()

        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def setupUi(self, mainwindow):
        super().setupUi(mainwindow)
        self.left_menubar = QMenuBar(self)
        self.right_menubar = QMenuBar(self)
        self.menu_icon = QMenu(self)
        self.menu_filter = QMenu(self)
        self.act_close = QAction(self)
        self.act_minimize = QAction(self)
        self.act_restore = QAction(self)
        self.init_custom_tilebar()

    def init_custom_tilebar(self):
        self.menubar.installEventFilter(self)
        self.init_left_menu()
        self.init_right_menu()

    def eventFilter(self, obj: QObject, _event: QMouseEvent):
        if _event.type() == QEvent.MouseButtonPress:
            self.curpos = _event.pos()

        if _event.type() == QEvent.MouseMove:
            if _event.buttons() & Qt.LeftButton:
                offset = _event.pos()
                self.move(self.pos() + offset - self.curpos)
        return super().eventFilter(obj, _event)

    def init_left_menu(self):
        pass

    def init_right_menu(self):
        pass
        self.act_close.setIcon(QIcon("icons/closeicon.png"))
        self.act_close.triggered.connect(self.close)

        self.act_minimize.setIcon(QIcon("icons/minimize.png"))
        self.act_minimize.triggered.connect(self.showMinimized)

        self.act_restore.setIcon(QIcon("icons/restore.png"))
        self.act_restore.triggered.connect(self.trigger_restore)

        self.right_menubar.addAction(self.act_minimize)
        self.right_menubar.addAction(self.act_restore)
        self.right_menubar.addAction(self.act_close)
        self.menubar.setCornerWidget(self.right_menubar, Qt.TopRightCorner)

    def trigger_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

