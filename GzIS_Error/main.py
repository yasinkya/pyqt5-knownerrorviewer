from PyQt5.QtWidgets import QApplication

from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.classes import Main_Window
from GzIS_Error.classes.MainWindow import MainWindow
import sys
import argparse

parser = argparse.ArgumentParser(description="insert path as str of jsons' folder")
parser.add_argument("path", type=str, help="path of jsons'")
args = parser.parse_args()


def main():
    global_variables.folder = args.path

    gzis_funcs.read_paths()
    app = QApplication(sys.argv)
    # win = Main_Window.Window()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


main()
