# * Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# * После каждого ввода добавляйте новую информацию в
# JSON файл.
# * Пользователи группируются по уровню доступа.
# * Идентификатор пользователя выступает ключём для имени.
# * Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# * При перезапуске функции уже записанные в файл данные
# должны сохраняться.

__all__ = ["func"]

import json
import os


def func(file_json: str):
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            dct = json.load(f)
        id_lst = [i for v in dct.values() for i in v]

    else:
        dct = {str(i): {} for i in range(1, 8)}
        id_lst = []

    while True:
        data = input('Введите через пробел имя, id, уровень доступа:\nДля выхода нажмите Enter\n')
        if not data:
            break
        user_name, u_id, access = data.split()
        if u_id not in id_lst:
            dct.setdefault(access, {u_id: user_name})[u_id] = user_name
            id_lst.append(u_id)
        else:
            print("Пользователь с таким id уже есть в базе")

    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(dct, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    func('HW_8/files/users.json')