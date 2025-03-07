from PySide6.QtWidgets import QApplication, QMainWindow
from windows.base.main_window_ui import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self._counter = 0
        self._one_click = 1
        self.btn_click.clicked.connect(self.plus_click)
        self.btn_open_settings.clicked.connect(self.open_settings_page)
        self.btn_open_shop.clicked.connect(self.open_shop_page)
        self.btn_plus_1.clicked.connect(lambda: self.plus_one_click(1))

    def open_settings_page(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_settings)

    def open_shop_page(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_shop)

    def plus_click(self) -> None:
        new_count = self.get_count() + self.get_one_click()
        self.set_count(new_count)
        self.set_label_count(str(new_count))

    def plus_one_click(self, value: int) -> None:
        new_one_click = self.get_one_click() + value
        self.set_one_click(new_one_click)

    def set_one_click(self, value: int) -> None:
        self._one_click = value

    def get_count(self) -> int:
        return self._counter

    def get_count_label(self) -> int:
        return int(self.count.text())

    def get_one_click(self) -> int:
        return self._one_click

    def set_label_count(self, value: str) -> None:
        self.count.setText(value)

    def set_count(self, value: int) -> None:
        self._counter = value


def start_app():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())