from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
import TreeWidget
import jsonPy_global


class New(QTableWidget):
    def __init__(self, itr):
        super(New, self).__init__()

        self.itr = itr
        self.keys = self.key_merge()
        self.init_widget()

    def init_widget(self):
        self.setColumnCount(len(self.keys))
        self.setHorizontalHeaderLabels(self.keys)
        # rows
        for i, data in enumerate(self.itr):
            self.insertRow(i)
            for j, key in enumerate(self.keys):
                # insert items
                item = QTableWidgetItem()
                if isinstance(data.get(key), dict):
                    # tree widget insert
                    treewidget = TreeWidget.New(data.get(key), i)
                    treewidget.setHeaderHidden(True)
                    self.setCellWidget(i, j, treewidget)
                    pass
                else:
                    item.setText(str(data.get(key)))
                self.setItem(i, j, item)
                self.verticalHeader().setDefaultSectionSize(50)
                self.horizontalHeader().setDefaultSectionSize(150)
                self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # set cell clicked
        self.cellClicked.connect(self.clicked_event)

    def clicked_event(self, row, col):
        for data in jsonPy_global.jsondata["feeds"]:

            for key, val in data.items():
                if self.itr == val:
                    print(val)

    def key_merge(self):
        keys = []
        for _dict in self.itr:
            keys += list(set(_dict.keys()) - set(keys))
        return keys
