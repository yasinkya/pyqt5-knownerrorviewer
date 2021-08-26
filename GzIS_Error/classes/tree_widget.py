from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class CreateTree(QTreeWidget):
    def __init__(self, data, col):
        super(CreateTree, self).__init__()
        self.data, self.col = data, col

        self.init_widget()

    def init_widget(self):
        for i, key in enumerate(self.data.keys()):
            self.addTopLevelItem(QTreeWidgetItem())
            self.topLevelItem(i).setText(self.col, key)
            self.topLevelItem(i).addChild(QTreeWidgetItem())
            self.topLevelItem(i).child(0).setText(self.col, str(self.data[key]))

