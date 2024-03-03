from PyQt6.QtWidgets import QMainWindow

from main_window_ui import Ui_MainWindow
from users import get_logins, get_password, get_user_data
from login_window_ui import Ui_LoginWindow
from config import set_config, read_config


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.config = read_config('config.txt')

        self.users_data = get_user_data(self.config['login'])

        if self.users_data is not None:
            self.set_info()

    def set_info(self):
        self.ui.label_6.setText(str(self.users_data['id']))
        self.ui.label_7.setText(self.users_data['login'])
        self.ui.label_8.setText(self.users_data['password'])
        self.ui.label_9.setText(self.users_data['name'])
        self.ui.label_10.setText(self.users_data['last_name'])


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginWindow()

        self.ui.setupUi(self)

        self.ui.login_btn.clicked.connect(self.login_btn_clicked)

        self.main_window = MainWindow()

        if not self.is_authed():
            print('Not Authed')
            self.show()
        else:
            self.main_window.show()
            print('Authed')

    def login_btn_clicked(self):
        login, password = self.ui.login, self.ui.password

        remember_me = self.ui.rememberMe

        if login.text() in get_logins():
            if password.text() == get_password(login.text()):
                if remember_me.isChecked():
                    set_config('config.txt', 'login', login.text())
                    self.close()
                    self.main_window.show()
                    print('authed with save')
                else:
                    print('authed without save')
                    self.main_window.show()
                    self.close()
            else:
                print('not ok (неверный пвроль)')
        else:
            print('not ok (неверный логин)')

    def is_authed(self) -> bool:
        cfg = read_config('config.txt')

        return cfg['login'] != 'None'
