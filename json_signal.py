from os import close, read
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys,json,importlib
import uis.tabwidget as tabWidget

class NewWindow(QMainWindow):
    def __init__(self,cntr_x,cntr_y,width, height):
        super(NewWindow,self).__init__()

        self.setGeometry(cntr_x,cntr_y,width, height)
        self.setWindowTitle("JSON OOP SIGNAL")
        self.initUI()

    def initUI(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("text")
        self.label.move(50,50)

        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("button")
        self.b1.clicked.connect(self.clicked)

        # self.tabbar=tabWidget.Ui_MainWindow()
        # self.tabbar.setupUi(self)
        

    def clicked(self):
        self.label.setText(str(readJson("jsons/employee.json")))
        self.b1.isEnabledTo=False
        self.update()

    def update(self):
        self.label.adjustSize()

    


def window():
    app=QApplication(sys.argv)

    cntr_p= QDesktopWidget().availableGeometry().center()
    scr_res=app.desktop().screenGeometry()
    
    width, height = int(scr_res.width()/2.5),int(scr_res.height()/2.5)
    cntr_x,cntr_y=cntr_p.x()-width/2,cntr_p.y()-height/2

    win=NewWindow(cntr_x,cntr_y,width, height)

    win.show()
    sys.exit(app.exec())


def readJson(jsonPath):
    f=open(jsonPath,"r")
    data=json.loads(f.read())
    f.close()
    return parsedJson(data)
    
def parsedJson(jsonData):
    list=[]
    for i in jsonData["feeds"]:
        list.append(i["id"])

    return list

    
window()
