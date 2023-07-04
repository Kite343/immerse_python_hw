# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

__all__ = ["new_json_file"]

import json


def new_json_file(file_name: str, json_f):
    dict_res = {}
    with (open(file_name, 'r', encoding='utf-8') as f,
          open(json_f, 'w', encoding='utf-8') as json_f):
        lines = f.readlines()
        for line in lines:
            name, num = line.split()
            dict_res[name.capitalize()] = num.strip()

        json.dump(dict_res, json_f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    new_json_file('HW_8/files/HW_7_files/result.txt', 'HW_8/files/name_num.json')

    