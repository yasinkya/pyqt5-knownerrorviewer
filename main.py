import sys
import argparse
import globvars
import gzis_funcs
from PyQt5.QtWidgets import QApplication
from classes.Main_UI import MainWindow

parser = argparse.ArgumentParser(description="insert path as str of jsons' folder")
parser.add_argument("path", type=str, help="path of jsons'")
args = parser.parse_args()


def main():
    globvars.folder = args.path
    gzis_funcs.read_paths()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


main()
