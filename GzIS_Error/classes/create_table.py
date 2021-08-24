from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class NewTableWidget(QTableWidget):
    def __init__(self, data):
        super(NewTableWidget, self).__init__()
        self.init_widget()

    def init_widget(self):
        with open("UIs/tablewidget_style.css", "r") as sheet:
            self.setStyleSheet(sheet.read())

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["yaska", "table", "tab"])

        self.insertRow(0)
        item = QTableWidgetItem()
        item.setText("helooo")
        self.setItem(0, 0, item)