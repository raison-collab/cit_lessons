from PyQt6.QtWidgets import QLineEdit, QCheckBox

from config import set_config
from lesson_11.config import read_config
from login_window_ui import Ui_MainWindow

import loader


def get_field(ui: Ui_MainWindow) -> list[QLineEdit]:
    return [
        ui.login,
        ui.password,
    ]


def get_checkboxes(ui: Ui_MainWindow) -> list[QCheckBox]:
    return [
        ui.rememberMe
    ]


def login_btn_clicked():
    fields = get_field(loader.login_window_ui)

    login, password = fields[0], fields[1]

    remember_me = get_checkboxes(loader.login_window_ui)[0]

    if login.text() == 'Daniil' and password.text() == '12345':
        if remember_me.isChecked():
            set_config('config.txt', 'login', login.text())
            set_config('config.txt', 'password', password.text())
            print('authed with save')
        else:
            print('authed without save')
    else:
        print('not ok')


def is_authed() -> bool:
    cfg = read_config('config.txt')

    return cfg['login'] != 'None'


def logic(ui: Ui_MainWindow) -> bool:
    login_btn = ui.login_btn

    login_btn.clicked.connect(login_btn_clicked)

    return is_authed()


"""
1) получить знач поля логин
2) получить знач поля пароль
3) сравнить поле логин с заданным знач и сравнить поле пароль с зад знач
4) если верно, то выводишь в консоль "ок", если нет, то "неверно"
"""