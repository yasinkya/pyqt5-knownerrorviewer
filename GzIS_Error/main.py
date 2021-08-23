from PyQt5.QtWidgets import QApplication
from classes import main_window as ui
import sys


def main():
    app = QApplication(sys.argv)
    win = ui.MainWindow()
    win.show()
    sys.exit(app.exec())


main()
