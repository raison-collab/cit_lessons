import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from utils.check_fields import check_fields


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


def main():
    app = QApplication(sys.argv)

    main_w = MainWindow()
    main_w.show()

    sys.exit(app.exec())


main()
