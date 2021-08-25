from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy, QAbstractScrollArea, QAbstractItemView, \
    QHeaderView


def init_widget(self: QTableWidget, data):
    headers = key_merge(data)
    with open("UIs/tablewidget_style.css", "r") as sheet:
        self.setStyleSheet(sheet.read())

    # set row, col and their resize
    self.setColumnCount(len(headers))
    self.setHorizontalHeaderLabels(headers)

    self.setRowCount(len(data.keys()))
    self.setVerticalHeaderLabels(data.keys())

    self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    for r, row in enumerate(data):
        for c, col in enumerate(headers):
            item = QTableWidgetItem()
            item.setText(str(data[row][col]))
            self.setItem(r, c, item)


def key_merge(data):
    keys = []
    for key in data.keys():
        keys += list(set(data[key].keys()) - set(keys))
    return keys




# class NewTableWidget(QTableWidget):
#     def __init__(self, data):
#         super(NewTableWidget, self).__init__()
#         self.data = data
#         self.headers = self.key_merge()
#         self.init_widget()
#
#     def init_widget(self):
#         with open("UIs/tablewidget_style.css", "r") as sheet:
#             self.setStyleSheet(sheet.read())
#
#         # set row, col and their resize
#         self.setColumnCount(len(self.headers))
#         self.setHorizontalHeaderLabels(self.headers)
#
#         self.setRowCount(len(self.data.keys()))
#         self.setVerticalHeaderLabels(self.data.keys())
#
#         self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
#
#         for r, row in enumerate(self.data):
#             for c, col in enumerate(self.headers):
#                 item = QTableWidgetItem()
#                 item.setText(str(self.data[row][col]))
#                 self.setItem(r, c, item)
#
#     def key_merge(self):
#         keys = []
#         for key in self.data.keys():
#             keys += list(set(self.data[key].keys()) - set(keys))
#         return keys
