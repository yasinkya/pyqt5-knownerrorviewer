from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy, QAbstractScrollArea, QAbstractItemView, \
    QHeaderView


class NewTableWidget(QTableWidget):
    def __init__(self, data):
        super(NewTableWidget, self).__init__()
        self.data = data
        self.headers = self.key_merge()
        self.init_widget()

    def init_widget(self):
        with open("UIs/tablewidget_style.css", "r") as sheet:
            self.setStyleSheet(sheet.read())

        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)

        # set rows

        self.setRowCount(len(self.data.keys()))
        print(self.rowCount())
        self.setVerticalHeaderLabels(self.data.keys())

        # size policy
        # self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # # tableview.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum) # ---
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)  # +++

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for r, row in enumerate(self.data):
            for c, col in enumerate(self.headers):
                item = QTableWidgetItem()
                item.setText(str(self.data[row][col]))
                self.setItem(r, c, item)


        # self.insertRow(0)
        # item = QTableWidgetItem()
        # item.setText("helooo")
        # self.setItem(0, 0, item)

    def key_merge(self):
        keys = []
        for key in self.data.keys():
            keys += list(set(self.data[key].keys()) - set(keys))
        return keys
