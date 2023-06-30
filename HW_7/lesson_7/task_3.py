# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

__all__ = ["read_per_line"]

import typing

def read_per_line(file_obj: typing.TextIO):
    line = file_obj.readline()
    if line == '':
        file_obj.seek(0)
        line = file_obj.readline()

    return line[: -1]


def mult(names, numbers, result):
    with  (
        open(names, 'r', encoding="utf-8") as f_names,
        open(numbers, 'r', encoding="utf-8") as f_numbers,
        open(result, 'w', encoding="utf-8") as f_result
    ):
        len_names = sum(True for _ in f_names)
        len_numbers = sum(True for _ in f_numbers)

        for _ in range(max(len_names, len_numbers)):
            name = read_per_line(f_names)
            num_line = read_per_line(f_numbers)
            num_1, num_2 = map(float, num_line.split('|'))
            res = num_1 * num_2
            if res < 0:
                f_result.write(f"{name.lower()} {abs(res)}\n")
            else:
                f_result.write(f"{name.upper()} {round(res)}\n")




if __name__ == '__main__':
    mult("HW_7\\files\\names.txt", "HW_7\\files\\numbers.txt", "HW_7\\files\\result.txt")

