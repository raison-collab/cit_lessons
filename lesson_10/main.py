import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

import loader
import login_window

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # init window
    login_window_ = QMainWindow()
    loader.login_window_ui.setupUi(login_window_)
    login_window_.show()

    # load login window logic
    login_window.logic(loader.login_window_ui)

    sys.exit(app.exec())
