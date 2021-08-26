from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class CreateTree(QTreeWidget):
    def __init__(self, data, col):
        super(CreateTree, self).__init__()
        self.data, self.col = data, col

        self.init_widget()

    def init_widget(self):
        _childs = ["failType", "isAccepted"]

        for i, key in enumerate(self.data.keys()):
            self.addTopLevelItem(QTreeWidgetItem())
            self.topLevelItem(i).setText(0, key)
            for j, _key in enumerate(_childs):
                self.topLevelItem(i).addChild(QTreeWidgetItem())
                self.topLevelItem(i).child(j).setText(0, f"{_key:10s}: {self.data[key][_key]}")
                # self.topLevelItem(i).child(j).addChild(QTreeWidgetItem())
                # self.topLevelItem(i).child(j).child(0).setText(col, str(self.data[key][_key]))
