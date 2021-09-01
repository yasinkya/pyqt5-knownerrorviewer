from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractScrollArea, QSizePolicy
from GzIS_Error.classes import tree_widget
import webbrowser


def init_widget(table: QTableWidget, data):
    table.clear()
    table.setColumnCount(0)
    table.setRowCount(0)

    with open("UIs/tablewidget_style.css", "r") as sheet:
        table.setStyleSheet(sheet.read())
    # set row, col and their resize
    table.insertColumn(0)
    table.setRowCount(len(data))
    for row, val in enumerate(data):
        item = QTableWidgetItem()
        item.setText(val)
        item.setTextAlignment(Qt.AlignCenter)
        table.setItem(row, 0, item)

    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.verticalHeader().setMaximumSectionSize(90)
    table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
    table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)



