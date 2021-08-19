from PyQt5.QtWidgets import QApplication
import ui_GzIs_main as ui
import sys


def main():
    app = QApplication(sys.argv)
    win = ui.Ui_MainWindow()
    win.show()
    sys.exit(app.exec())


main()