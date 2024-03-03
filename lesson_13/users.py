import csv
from typing import Optional, Any


def get_users(path: str) -> list[list[str]]:
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        return list(reader)[1:]


def get_logins() -> list[str]:
    return [row[1] for row in get_users('users.csv')]


def get_password(login: str) -> Optional[str]:
    users_data = get_users('users.csv')

    for row in users_data:
        if row[1] == login:
            return row[2]

    return None


def get_user_data(login: str) -> Optional[dict[str, Any]]:
    users_data = get_users('users.csv')

    for row in users_data:
        if row[1] == login:
            return {
                'id': int(row[0]),
                'login': row[1],
                'password': row[2],
                'name': row[3],
                'last_name': row[4]
            }

    return None
