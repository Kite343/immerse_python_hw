# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

__all__ = ["task_1"]

from random import randint, uniform

MIN = -1000
MAX = 1000

def task_1(count_row, filename):
    with open(filename, 'a', encoding="utf-8") as f:
        for _ in range(count_row):
            f.write(f"{randint(MIN, MAX + 1)}|{round(uniform(MIN, MAX + 1), 2)}\n")

if __name__ == '__main__':
    task_1(5, "HW_7\\files\\numbers.txt")

