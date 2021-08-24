from PyQt5.QtWidgets import QTabWidget


class New(QTabWidget):
    def __init__(self):
        super(New, self).__init__()
        self.init_widget()

    def init_widget(self):
        self.setObjectName("TabWidget")
        with open("UIs/GzIS_tabwid_styel_sheet.css", "r") as twsheet:
            self.setStyleSheet(str(twsheet.read()))
            self.setCurrentIndex(-1)

    def set_main_tabs(self, data):
        pass