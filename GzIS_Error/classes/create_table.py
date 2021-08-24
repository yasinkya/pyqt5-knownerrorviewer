from PyQt5.QtWidgets import QTableWidget


class NewTableWidget(QTableWidget):
    def __init__(self, data):
        super(NewTableWidget, self).__init__()

    def init_widget(self):