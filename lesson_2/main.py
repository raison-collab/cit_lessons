from utils.check_fields import check_fields



def main():
    login = input('Login - ')
    password = input('Password - ')

    check_fields_ = check_fields(login, password)

    if check_fields_:
        print('Все ок')
        return

    print('Проверка не прошла')


main()
