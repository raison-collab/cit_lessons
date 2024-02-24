import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

import loader
import login_window

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # init window
    login_window_ = QMainWindow()
    loader.login_window_ui.setupUi(login_window_)
    # load login window logic
    if not login_window.logic(loader.login_window_ui):
        login_window_.show()
        print('not authed')

    else:
        print('authed')

    sys.exit(app.exec())
