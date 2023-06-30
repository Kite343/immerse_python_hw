# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

__all__ = ["task_4"]

import os
import random
import string


def task_4(extension='bin', min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count_file=42):
    for _ in range(count_file):
        name_len = random.randint(min_len_name, max_len_name)
        file_size = random.randint(min_byte, max_byte)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_len)) + '.' + extension
        # random_bytes = os.urandom(file_size)
        random_bytes = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode('UTF-8')

        with open("HW_7\\files\\task_4\\" + file_name, "wb") as file:
            file.write(random_bytes)


if __name__ == '__main__':
    task_4(extension='txt', count_file=3)
    task_4(extension='bin', count_file=3)