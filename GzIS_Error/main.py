from PyQt5.QtWidgets import QApplication
import ui_main1 as ui
import sys


def main():
    app = QApplication(sys.argv)
    win = ui.MainWindow()
    win.show()
    sys.exit(app.exec())


main()
