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

from collections import namedtuple
import logging
import os
import argparse


# или лучше filemode='a'?
FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(filename='log_dir.log', format=FORMAT, style='{', 
                    filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def dir_info(dir_):
    # print(*os.walk(dir_))
    Object_in_dir = namedtuple('Object_in_dir', ['name', 'ext_or_folder', 'parent_folder'])
    # res = []

    for folder in os.walk(dir_):
        parent_fold = folder[0].rsplit("\\", 1)[-1]
        # print(parent_fold)

        for file in folder[2]:
            new_ob =  Object_in_dir(file.rsplit(".", 1)[0], 
                                    file.rsplit(".", 1)[-1], parent_fold)
            logger.info(f'Data: {new_ob}')
            # res.append(new_ob)
            # print(new_ob)

        for fold in folder[1]:
            new_ob = Object_in_dir(fold, 'folder', parent_fold)
            logger.info(f'Data: {new_ob}')
            # res.append(new_ob)
            # print(new_ob)

def parser():
    parser = argparse.ArgumentParser(description='Folder parser info')
    parser.add_argument('-f', metavar='folder', default=os.getcwd(), help="enter folder")
    args = parser.parse_args()
    print(args)
    dir_info(args.f)

if __name__ == "__main__":
    parser()

    
    # python HW_15\\hw_task_var_1.py -f "путь к папке"
    #  или
    # python HW_15\\hw_task_var_1.py