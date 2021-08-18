from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView


class New(QTableWidget):
    def __init__(self, itr):
        super(New, self).__init__()

        self.itr = itr
        self.keys = self.key_merge()
        self.init_ui()

    def init_ui(self):
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
