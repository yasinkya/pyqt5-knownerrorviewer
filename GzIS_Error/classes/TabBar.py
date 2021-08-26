from PyQt5.QtWidgets import QTabBar


class CreateTabbar(QTabBar):
    def __init__(self):
        super(CreateTabbar, self).__init__()
        self.init_widget()

    def init_widget(self):
        with open("UIs/GzIS_tabwid_styel_sheet.css", "r") as twsheet:
            self.setStyleSheet(str(twsheet.read()))
