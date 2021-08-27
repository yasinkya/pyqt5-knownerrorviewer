from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractScrollArea, QSizePolicy, QLayout
from GzIS_Error.classes import tree_widget
import webbrowser


def init_widget(table: QTableWidget, data):
# def init_widget(lay: QLayout, data):
#     table = QTableWidget()
    headers = ["testCount", "passCount", "failCount", "link"]
    with open("UIs/tablewidget_style.css", "r") as sheet:
        table.setStyleSheet(sheet.read())

    # set row, col and their resize
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)

    table.setRowCount(len(data.keys()))
    table.setVerticalHeaderLabels(data.keys())

    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.verticalHeader().setMaximumSectionSize(90)
    table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
    table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    table.horizontalHeader().sectionClicked.connect(horizontal_clicked)

    for c, col in enumerate(headers):
        for r, row in enumerate(data):
            if col == "failCount":
                tree = tree_widget.CreateTree(data[row]["failTests"], c)
                tree.setHeaderLabel(f"{data[row][col]} - Failed Tests")
                tree.header().setDefaultAlignment(Qt.AlignCenter)
                table.setCellWidget(r, c, tree)
                table.verticalHeader().setSectionResizeMode(r, QHeaderView.ResizeToContents)
            else:
                item = QTableWidgetItem()
                item.setText(str(data[row].get(col)))
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(r, c, item)

    table.cellClicked.connect(lambda idx_r, idx_c: _table_click_trigger(idx_r, idx_c, table))
    # table.currentCellChanged.connect(lambda idx_r, idx_c: _table_click_trigger(idx_r, idx_c, table))
    # lay.addWidget(table)

def _table_click_trigger(row, col, table: QTableWidget):
    if table.horizontalHeaderItem(col).text() == "link":
        print(table.item(row, col).text())
        if table.item(row, col).text() != "None":
            webbrowser.open("https://www.qt.io/")

        else:
            print(row)
    else:
        print(table.cellWidget(row, col))

def horizontal_clicked():
    print("clicked")
