def read_config(path: str):
    with open(path, 'r') as file:
        content = file.readlines()

    data = {}

    for row in content:
        el = row.split('-')  # ['login', 'Daniil']
        key, value = el[0], el[1].replace('\n', '')

        data[key] = value

    return data


def set_config(path: str, key: str, value: str):
    data = read_config(path)

    data[key] = value

    s = ''

    for k in data:
        s += f'{k}-{data[k]}\n'

    with open(path, 'w') as file:
        file.write(s)
