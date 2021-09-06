import sys
import argparse
import gzis_funcs
import global_variables
import json_func
from classes import Main_Window
from PyQt5.QtWidgets import QApplication
from classes.MainWindow import MainWindow

parser = argparse.ArgumentParser(description="insert path as str of jsons' folder")
parser.add_argument("path", type=str, help="path of jsons'")
args = parser.parse_args()


def main():
    global_variables.folder = args.path
    json_func.read_paths()
    app = QApplication(sys.argv)
    # win = Main_Window.Window()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


main()
