from PyQt6.QtWidgets import QLineEdit, QCheckBox

from lesson_10.login_window_ui import Ui_MainWindow

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
        pass
    else:
        pass


def logic(ui: Ui_MainWindow):
    login_btn = ui.login_btn

    login_btn.clicked.connect(login_btn_clicked)


"""
1) получить знач поля логин
2) получить знач поля пароль
3) сравнить поле логин с заданным знач и сравнить поле пароль с зад знач
4) если верно, то выводишь в консоль "ок", если нет, то "неверно"
"""