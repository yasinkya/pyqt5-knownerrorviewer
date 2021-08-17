from PyQt5.QtWidgets import QApplication
import sys
import Window
import jsonPy_global
import functions


def main():
    # global variable for json data
    jsonPy_global.jsondata = functions.read_json()

    app = QApplication(sys.argv)
    # window size
    res = app.desktop().availableGeometry()
    w, h = res.width() / 2.5, res.height() / 2

    win = Window.New(w, h)
    win.show()
    sys.exit(app.exec())


main()

