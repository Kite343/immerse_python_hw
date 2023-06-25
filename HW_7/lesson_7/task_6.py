# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

__all__ = ["create_dif_files", "create_files"]

import os
import random
import string


def create_files(dir_ = os.getcwd(), extension='bin', min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count_file=42):
    for _ in range(count_file):
        name_len = random.randint(min_len_name, max_len_name)
        file_size = random.randint(min_byte, max_byte)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_len)) + '.' + extension
        
        while os.path.exists(os.path.join(dir_, file_name)):
            file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_len)) + '.' + extension
            
        random_bytes = os.urandom(file_size)
        random_bytes = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode('UTF-8')

        with open(dir_ + file_name, "wb") as file:
            file.write(random_bytes)

def create_dif_files(dir_, **kwargs):
    if not os.path.exists(dir_):
        os.mkdir(dir_)
    for ext, num in kwargs.items():
        create_files(dir_, extension=ext, count_file=num)


if __name__ == '__main__':
    create_dif_files("HW_7\\files\\task_6\\", txt=2, bin=4, png=3)