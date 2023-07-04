# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
#  Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
#  Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

__all__ = ["pickle_to_csv"]

import pickle
import csv


def pickle_to_csv(pickle_file, csv_file):
    with (open(pickle_file, 'rb') as f_p,
          open(csv_file, 'w', newline='', encoding='utf-8') as f_csv):
        my_dict = pickle.load(f_p)
        # print(my_dict)
        keys = [k for k in my_dict[0].keys()]
        # print(keys)
        csv_write = csv.DictWriter(f_csv,fieldnames=keys, dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(my_dict)


if __name__ == '__main__':
    pickle_to_csv('HW_8/files/users_new.pickle', 'HW_8/files/users_new_task_6.csv')