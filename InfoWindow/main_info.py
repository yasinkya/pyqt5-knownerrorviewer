from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import Info


def main(data):
    app = QApplication(sys.argv)

    win = Info.New(data)
    win.show()
    sys.exit(app.exec())

main()
