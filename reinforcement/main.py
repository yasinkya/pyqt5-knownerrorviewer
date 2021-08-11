from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDesktopWidget
import sys, Window

def win():
    app=QApplication(sys.argv)

    cp=QDesktopWidget().availableGeometry().center()
    scres= app.desktop().availableGeometry()

    w,h=int(scres.width()/2.5),int(scres.height()/2.5)
    cx,cy=cp.x()-w/2,cp.y()-h/2

    win=Window.NewWindow(cx,cy,w,h)

    win.show()
    sys.exit(app.exec())

win()