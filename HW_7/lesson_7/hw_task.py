# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. 
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. 
#   Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

#  Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

__all__ = ["rename_files"]

import os


def rename_files(new_name, ext, new_ext, dir_ = os.getcwd()):
    if not os.path.exists(dir_):
        print("the folder is missing")
        return
    os.chdir(dir_)

    list_files = list(filter(lambda file: os.path.isfile(file) and file.split('.')[-1] == ext, os.listdir()))
    
    position = 1
    for file in list_files:
        new_filename = f"{file.rsplit('.', 1)[0]}_{new_name}_{position}.{new_ext}"
        os.rename(file, new_filename)
        position += 1

    pass

if __name__ == '__main__':
    rename_files("temp", "bin", "txt", "HW_7\\files\\task_6")
    rename_files("temp", "bin", "txt", "HW_7\\files\\task_4")
