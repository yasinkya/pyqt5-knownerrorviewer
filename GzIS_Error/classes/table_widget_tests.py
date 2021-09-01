from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractScrollArea, QSizePolicy
from GzIS_Error.classes import tree_widget
import webbrowser


def init_widget(table: QTableWidget, data):

    headers = ["testCount", "passCount", "failCount", "defectNo"]
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
                table.item(r, c).setFlags(Qt.ItemIsEnabled)

    if table.receivers(table.cellClicked) == 0:
        table.cellClicked.connect(lambda idx_r, idx_c: _table_click_trigger(idx_r, idx_c, table))

    table.horizontalHeader().sectionClicked.connect(lambda idcol: horizontal_clicked(idcol, table))


def _table_click_trigger(row, col, table: QTableWidget):
    if table.horizontalHeaderItem(col).text() == "defectNo":
        # print(table.item(row, col).text())
        if (item_id := table.item(row, col).text()) != "None":
            target_addr = f"https://jazz/ccm/web/projects/GIS%20(Change%20Management)" \
                          f"#action=com.ibm.team.workitem.viewWorkItem&id={item_id}"
            webbrowser.open(target_addr)


def horizontal_clicked(col, table: QTableWidget):
    # todo filter by clicked cells
    if not table.isSortingEnabled():
        table.sortItems(col, 0)
        table.setSortingEnabled(True)
    else:
        table.sortItems(col, 1)
        table.setSortingEnabled(False)
