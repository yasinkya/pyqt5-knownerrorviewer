from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,200,960,540)
        self.setWindowTitle("OOP")
        self.initUI()
    
    def initUI(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("label self")
        self.label.move(50,50)

        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText("button self")
        self.btn.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("clicked self button")

def window():
    app=QApplication(sys.argv)
    win= MyWindow()

    win.show()
    sys.exit(app.exec())


window()
