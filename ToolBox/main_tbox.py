from PyQt5.QtWidgets import QApplication
import sys
import window
import jsonPy_global as glb
import json


def main():
    glb.jsondata = json.loads(open("../jsons/employee.json", "r").read())
    app = QApplication(sys.argv)
    win = window.Main_Window()

    win.show()
    sys.exit(app.exec())


main()

