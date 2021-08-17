from PyQt5.QtWidgets import QWidget, QToolBox, QLayout


def new_page(layout: QLayout, tbox: QToolBox, data):
    for i in range(len(data)):
        page = QWidget()
        tbox.addItem(page, str(data[i]))
    layout.addWidget(tbox)
