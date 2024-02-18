import sys

from PyQt6.QtWidgets import QLineEdit, QApplication

from lesson_9.m import Ui_MainWindow

app = QApplication(sys.argv)


def btn_click():
    login_t = login_field.text()
    password_t = password_filed.text()

    if login_t == 'Usr' and password_t == '123':

        print('ОК', check_box.isChecked())
    else:
        print('Неверно')


main_window = Ui_MainWindow()
main_window.setupUi(main_window)

password_filed = main_window.lineEdit_2
login_field = main_window.login

btn = main_window.pushButton

check_box = main_window.checkBox

btn.clicked.connect(btn_click)

main_window.show()
sys.exit(app.exec())
