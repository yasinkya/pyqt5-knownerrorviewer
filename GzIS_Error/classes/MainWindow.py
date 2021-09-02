from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QMainWindow
from GzIS_Error import global_variables, gzis_funcs
from GzIS_Error.UIs.GzIS_main_window import Ui_MainWindow
from GzIS_Error.classes import table_widget_target, table_widget_tests


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def setupUi(self, MainWindow):
        super().setupUi(self)

        self.btn_palette.clicked.connect(self.btn_palette_trigger)
        self.check_exception.clicked.connect(self.check_target_trigger)
        self.tbar_headers.currentChanged.connect(self.tbar_changed_trigger)
        self.cbx_ar_pos.currentIndexChanged.connect(self.cbx_arpos_current_changed)
        self.cbx_jsons.currentIndexChanged.connect(self.cbx_paths_current_changed)
        self.cbx_ar_pos.setCurrentIndex(1)


    def cbx_arpos_current_changed(self):
        self.clear_contents()
        self.tbar_headers.blockSignals(False)
        gzis_funcs.sync_global_jsonfiles(self.cbx_ar_pos)
        self.cbx_jsons.sync_widget(global_variables.json_files)

    def cbx_paths_current_changed(self):
        if self.cbx_jsons.currentIndex() != -1:
            self.clear_contents()
            self.statusbar.addPermanentWidget(self.lbl_isaccept, 0)
            self.statusbar.addPermanentWidget(self.cbx_isaccept, 0)
            self.statusbar.showMessage(global_variables.current_path)
            self.tbar_headers.blockSignals(False)

            gzis_funcs.set_tabbar(f"{global_variables.folder}/{self.cbx_ar_pos.currentText()}/"
                                  f"{self.cbx_jsons.currentText()}", self.tbar_headers, False)

    def clear_contents(self):
        self.table_content.clear()
        self.table_content.setRowCount(0)
        self.table_content.setColumnCount(0)
        self.tbar_headers.blockSignals(True)
        while self.tbar_headers.count() > 0:
            self.tbar_headers.removeTab(0)

    def tbar_changed_trigger(self, idx):
        json_data = global_variables.current_jsondata[self.tbar_headers.tabText(idx)]
        # for test suites
        if not self.check_exception.isChecked():
            table_widget_tests.init_widget(self.table_content, json_data["tests"])
        # for target
        else:
            table_widget_target.init_widget(self.table_content, json_data)

    def btn_palette_trigger(self):
        palette = QPalette()
        if global_variables.is_light:
            palette.setBrush(self.backgroundRole(), QColor(45, 45, 45))
            global_variables.is_light = False
        else:
            palette.setBrush(self.backgroundRole(), QColor(220, 220, 220))
            global_variables.is_light = True
        self.setPalette(palette)

    def check_target_trigger(self):
        self.clear_contents()
        if self.check_exception.isChecked():
            self.set_cbx_enabled(False)
            self.set_table_header_visible(False)
            path = r"knownError\target.json"
            gzis_funcs.set_tabbar(path, self.tbar_headers, True)
            self.tbar_headers.blockSignals(False)
            table_widget_target.init_widget(self.table_content,
                                            global_variables.current_jsondata[self.tbar_headers.tabText(0)])
        else:
            self.set_cbx_enabled(True)
            self.set_table_header_visible(True)
            self.cbx_ar_pos.setCurrentIndex(0)

    def set_cbx_enabled(self, val: bool):
        self.cbx_jsons.setEnabled(val)
        self.cbx_ar_pos.setEnabled(val)

    def set_table_header_visible(self, val: bool):
        self.table_content.verticalHeader().setVisible(val)
        self.table_content.horizontalHeader().setVisible(val)



