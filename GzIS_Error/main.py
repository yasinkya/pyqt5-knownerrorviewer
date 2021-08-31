from PyQt5.QtWidgets import QApplication

import global_variables
from classes import Main_Window
import sys
import gzis_funcs
import argparse

parser = argparse.ArgumentParser(description="insert path as str of jsons' folder")
parser.add_argument("path", type=str, help="path of jsons'")
args = parser.parse_args()


def main():
    global_variables.folder = args.path

    gzis_funcs.read_paths()
    app = QApplication(sys.argv)
    win = Main_Window.Window()
    win.show()
    sys.exit(app.exec())


main()
