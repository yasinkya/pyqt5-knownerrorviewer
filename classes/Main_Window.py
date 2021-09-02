from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPalette, QColor
from UIs import GzIs_error_main
import global_variables, gzis_funcs
from classes import table_widget_tests, table_widget_target


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        main_ui = GzIs_error_main.UiMainWindow()
        main_ui.setup_ui(self)

        self.cbx_jsons = main_ui.cbx_jsons
        self.statusbar = main_ui.statusbar
        self.cbx_ar_pos = main_ui.cbx_ar_pos
        self.btn_palette = main_ui.btn_palette
        self.cbx_isaccept = main_ui.cbx_isaccept
        self.tbar_headers = main_ui.tbar_headers
        self.lbl_isaccept = main_ui.lbl_isaccept
        self.table_content = main_ui.table_content
        self.check_exception = main_ui.check_exception

        self.setup_widget()


    def setup_widget(self):
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
