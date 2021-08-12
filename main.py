from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDesktopWidget
import sys, Window

def main():
    app= QApplication(sys.argv)
    
    cp=QDesktopWidget().availableGeometry().center()
    res=app.desktop().availableGeometry()
    w,h=res.width()/2.5,res.height()/2.5
    x,y=cp.x()-w/2,cp.y()-h/2

    win=Window.New(x,y,w,h)
    win.show()
    sys.exit(app.exec())

main()
    
