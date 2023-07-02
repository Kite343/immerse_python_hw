# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

__all__ = ["json_csv"]

import csv
import json


def json_csv(jsonfile, csvfile):
    with(open(jsonfile, "r", encoding="utf-8") as json_f,
        open(csvfile, "w", newline='', encoding="utf-8") as csv_f):
        json_dict = json.load(json_f)
        rows = []
        for level, in_dict in json_dict.items():
            for a_id, name in in_dict.items():
                rows.append({'id': a_id, 'level': int(level), 'name': name})

        csv_write = csv.DictWriter(csv_f, fieldnames=['id', 'level', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    json_csv('HW_8/files/users.json', 'HW_8/files/users.csv')