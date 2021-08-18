from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class New(QTreeWidget):
    def __init__(self, data, x):
        super(New, self).__init__()
        self.data, self.x = data, x

        self.init_widget()

    def init_widget(self):
        for i, key in enumerate(self.data.keys()):
            item_top = QTreeWidgetItem(self)
            self.topLevelItem(i).setText(self.x, key)

            self.topLevelItem(i).insertChild(self.x, QTreeWidgetItem())
            self.topLevelItem(i).child(self.x).setText(self.x, self.data[key])

