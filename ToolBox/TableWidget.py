from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
import TreeWidget

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
                    pass
                else:
                    item.setText(str(data.get(key)))
                self.setItem(i, j, item)
                self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # set cell clicked

    def key_merge(self):
        keys = []
        for _dict in self.itr:
            keys += list(set(_dict.keys()) - set(keys))
        return keys
