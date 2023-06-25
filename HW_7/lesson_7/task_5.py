# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

__all__ = ["create_files", "create_dif_files"]

import os
import random
import string


def create_files(extension='bin', min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count_file=42):
    for _ in range(count_file):
        name_len = random.randint(min_len_name, max_len_name)
        file_size = random.randint(min_byte, max_byte)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_len)) + '.' + extension
        # random_bytes = os.urandom(file_size)
        random_bytes = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode('UTF-8')

        with open("HW_7\\files\\task_5\\" + file_name, "wb") as file:
            file.write(random_bytes)

def create_dif_files(**kwargs):
    for ext, num in kwargs.items():
        create_files(extension=ext, count_file=num)


if __name__ == '__main__':
    create_dif_files(txt=2, bin=4, png=3)
