from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy, QAbstractScrollArea, QAbstractItemView, \
    QHeaderView
from GzIS_Error.classes import tree_widget


def init_widget(table: QTableWidget, data):
    headers = ["testCount", "passCount", "failCount", "link"]
    with open("UIs/tablewidget_style.css", "r") as sheet:
        table.setStyleSheet(sheet.read())

    # set row, col and their resize
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)

    table.setRowCount(len(data.keys()))
    table.setVerticalHeaderLabels(data.keys())

    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    for c, col in enumerate(headers):
        for r, row in enumerate(data):
            if col == "failCount":
                tree = tree_widget.CreateTree(data[row]["failTests"], c)
                table.setCellWidget(r, c, tree)
                fails = data[row][col]
                tree.setHeaderLabel(f"{fails} - Failed Tests")
                tree.header().setDefaultAlignment(Qt.AlignCenter)
            else:
                item = QTableWidgetItem()
                item.setText(str(data[row].get(col)))
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(r, c, item)

