import json, importlib
"""
jsn=json.load(open("user.json"))
#print(jsn)

for i in jsn["users"]:
    print(i)
    #print(i["std"])


f=open("user.json","r")
js2=json.loads(f.read())
for i in js2["users"]:
    print(i)

a={}
k=0
while k<10:
    key ="dnmc"
    val="asd"
    a[key]=val
    k+=1

print(a)
"""
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow
import sys,json,importlib

#create window
def window():
    
    app= QApplication(sys.argv)
    win=QMainWindow()

    #screen orientation set
    cntr_p= QDesktopWidget().availableGeometry().center() 
    scr_res= app.desktop().screenGeometry()
    width, height = int(scr_res.width()/2.5),int(scr_res.height()/2.5)
    cntr_x,cntr_y=(cntr_p.x()-width/2),(cntr_p.y()-height/2)
    
    win.setGeometry(cntr_x,cntr_y,width,height)

    #window prps
    win.setWindowTitle("PYQT5")

    #Qlabel
    label=QtWidgets.QLabel(win)
    label.setText("Labesdfgsdfgsdl")
    label.move(10,10)

    #Signals & buttons
    button=QtWidgets.QPushButton(win)
    button.setText("Button")
    button.move(label.x()+50,label.y()+20)
    button.clicked.connect(btnclicked)

    win.show()
    sys.exit(app.exec())
    

def btnclicked():
    #actions
    print("button clicked")
window()


#json import
def readJson():
    jsonfile=json.load(open("user.json"))
    return str(jsonfile)




