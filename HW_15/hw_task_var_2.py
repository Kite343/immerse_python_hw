# 📌 Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя
# логирование.

# за основу взято дз из HW_8

__all__ = ["dir_info"]

from collections import namedtuple
import logging
import os
import argparse

# или лучше filemode='a'?
FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(filename='log_dir_1.log', format=FORMAT, style='{', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def dir_info(dir_):
    Object_in_dir = namedtuple('Object_in_dir', ['name', 'ext_or_folder','size', 'parent_folder'])

    # идем с конца в начало, для упрощения подсчета размера папок
    # 0 позиция - родительская папка
    # 1 позиция - список папок в родительской папке
    # 2 позиция - список файлов в папке
    size_folders = {}  # для подсчета размера папок
    for folder in os.walk(dir_, topdown=False):
        # имя родительской папки
        parent_fold = folder[0].rsplit("\\", 1)[-1]
        sum = 0

        # проходимся по файлам и записываем их данные
        # размер файла добавляем в сумму для определения размера папки
        # у файлов можно сразу записывать только имя раодительской папки
        # а не весь путь, т.к. больше мы к ним обращаться не будем
        for file in folder[2]:
            size = os.path.getsize(f'{folder[0]}\\{file}')
            sum += size
            new_ob =  Object_in_dir(file.rsplit(".", 1)[0], 
                                    file.rsplit(".", 1)[-1], size, parent_fold)
            logger.info(f'Data: {new_ob}')
            
        # проходимся по дочерним папкам
        # и добавляем их размер в сумму для родительской папки
        # значения берем из созданного словаря
        # 1 позиция - список папок в родительской папке проходимся по ней
        for fold in folder[1]:
            sum += size_folders[os.path.join(folder[0] ,fold)]

        # добавляем в словарь размер папки
        size_folders[folder[0]] = sum

        # добавляем саму родительскую папку как объект
        parent = folder[0].rsplit("\\", 2)
        parent = None if len(parent) == 1 else parent[-2]
        new_ob = Object_in_dir(folder[0].rsplit("\\", 1)[-1], 'folder', sum, parent)
        logger.info(f'Data: {new_ob}')
    
def parser():
    parser = argparse.ArgumentParser(description='Folder parser info')
    parser.add_argument('-f', metavar='folder', default=os.getcwd(), help="folder")
    args = parser.parse_args()
    print(args)
    dir_info(args.f)
    

if __name__ == '__main__':
    parser()

# python HW_15\\hw_task_var_2.py -f "путь к папке"
#  или
# python HW_15\\hw_task_var_2.py


# при большом количестве и глубине папок, такой код будет работать быстрее,
# чем для каждой папки проходится опять по всем папкам и файлам, для подсчета размера папки
# мы используем для этого уже ранее полученную информацию