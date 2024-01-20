def check_login_field(login: str) -> bool:
    return len(login.split()) == 1


def check_password_field(password: str) -> bool:
    return len(password.split()) == 1 and len(password) >= 8


def check_fields(filed1: str, field2: str) -> bool:
    check_login = check_login_field(filed1)
    check_password = check_password_field(field2)

    if check_login and check_password:
        return True
    return False

