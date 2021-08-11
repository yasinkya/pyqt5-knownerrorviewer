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
import sys


def window():
    app= QApplication(sys.argv)
    win=QMainWindow()

    cntr_p= QDesktopWidget().availableGeometry().center()
    print(cntr_p.x())
    scr_res= app.desktop().screenGeometry()
    width, height = int(scr_res.width()/4),int(scr_res.height()/4.5)
    cntr_x,cntr_y=(cntr_p.x()-width/2),(cntr_p.y()-height/2)
    
    win.setGeometry(cntr_x,cntr_y,width,height)
    win.setWindowTitle("PYQT5")

    

    win.show()
    sys.exit(app.exec())
    
window()



