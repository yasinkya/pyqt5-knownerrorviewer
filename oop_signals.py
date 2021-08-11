from PyQt5 import QtWidgetsi,QtCore
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))

window()
