# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку

__all__ = ["read_csv_as_pikle"]

import csv
import pickle


def read_csv_as_pikle(csv_file):
    with open(csv_file, 'r', encoding='utf-8', newline='') as csv_f:
        list_csv = [*csv.reader(csv_f, dialect='excel-tab')]
        # print(list_csv)
        dict_list_csv = [dict(zip(list_csv[0], list_csv[i]))
                         for i in range(1, len(list_csv))]
        # print(dict_list_csv)

        res = pickle.dumps(dict_list_csv)
        print(res)
        # print(pickle.loads(res))


if __name__ == '__main__':
    read_csv_as_pikle('HW_8/files/users_new_task_6.csv')