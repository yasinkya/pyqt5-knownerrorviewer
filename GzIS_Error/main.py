from PyQt5.QtWidgets import QApplication

from GzIS_Error import global_variables
from classes import Main_Window
import sys
import gzis_funcs


def main():
    global_variables.folder = "/home/yaska/Desktop/Jsons/knownError"
    gzis_funcs.read_paths()
    app = QApplication(sys.argv)
    win = Main_Window.Window()
    win.show()
    sys.exit(app.exec())


main()
