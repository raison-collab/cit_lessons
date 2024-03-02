from PyQt6.QtWidgets import QMainWindow

from login_window_ui import Ui_MainWindow
from config import set_config, read_config


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.login_btn.clicked.connect(self.login_btn_clicked)

        if not self.is_authed():
            print('Not Authed')
            self.show()
        else:
            print('Authed')

    def login_btn_clicked(self):
        login, password = self.ui.login, self.ui.password

        remember_me = self.ui.rememberMe

        if login.text() == 'Daniil' and password.text() == '12345':
            if remember_me.isChecked():
                set_config('config.txt', 'login', login.text())
                set_config('config.txt', 'password', password.text())
                print('authed with save')
            else:
                print('authed without save')
        else:
            print('not ok')

    def is_authed(self) -> bool:
        cfg = read_config('config.txt')

        return cfg['login'] != 'None'
