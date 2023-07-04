#  Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

__all__ = ['func']

import json
import pickle
import os


def func(dir_):
    json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
    
    for json_file in json_files:
        with (open(os.path.join(dir_, json_file), 'r', encoding='utf-8') as f_js,
              open(os.path.join(dir_, f"{json_file[:-4]}pickle"), 'wb') as f_p):
            # open(os.path.join(dir_, json_file.rsplit(".", 1)[0] + ".pickle"), 'wb') as f_p):
            pickle.dump(json.load(f_js), f_p)


if __name__ == '__main__':
    func("HW_8/files")
    with open('HW_8/files/users.pickle', 'rb') as f_pi:
        print(pickle.load(f_pi))