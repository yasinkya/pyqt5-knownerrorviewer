from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy

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
    # table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    for c, col in enumerate(headers):
        for r, row in enumerate(data):
            if col == "failCount":
                tree = tree_widget.CreateTree(data[row]["failTests"], c)
                tree.setHeaderLabel(f"{data[row][col]} - Failed Tests")
                tree.header().setDefaultAlignment(Qt.AlignCenter)
                table.setCellWidget(r, c, tree)
                table.setRowHeight(r, 70)
            else:
                item = QTableWidgetItem()
                item.setText(str(data[row].get(col)))
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(r, c, item)

    table.cellClicked.connect(lambda row, col: _table_click_trigger(row, col, table))


def _table_click_trigger(row, col, table: QTableWidget):
    import webbrowser
    if table.horizontalHeaderItem(col).text() == "link":
        print(table.item(row, col).text())
        webbrowser.open("https://www.youtube.com/watch?v=zGMgIdI9EkE")
