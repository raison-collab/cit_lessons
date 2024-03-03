import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from windows import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_window_ = LoginWindow()

    sys.exit(app.exec())
