from PyQt5.QtWidgets import QComboBox


class New(QComboBox):
    def __init__(self):
        super(New, self).__init__()
        self.init_widget()

    def init_widget(self):
        self.setObjectName("comboBox")
        with open("UIs/GzIs_cbx_style_sheet.css", "r") as cbxsheet:
            self.setStyleSheet(str(cbxsheet.read()))

    def sync_widget(self, data):
        self.clear()
        self.addItems(data)
        self.setCurrentIndex(-1)
        self.blockSignals(False)


