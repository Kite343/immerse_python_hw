# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

__all__ = ["dir_info"]

import json
import pickle
import csv
import os

def save_data_in_files(data, dir_, name_file):
    with (open(os.path.join(dir_, name_file + ".json"), 'w', encoding='utf-8') as json_f,
          open(os.path.join(dir_, name_file + ".csv"), 'w', newline='', encoding='utf-8') as csv_f, 
          open(os.path.join(dir_, name_file + ".pickle"), 'wb') as pickle_f): 
          json.dump(data, json_f, indent=4, ensure_ascii=False) 
          pickle.dump(data, pickle_f) 
          csv_write = csv.DictWriter(csv_f, fieldnames=[*data[0]]) 
          csv_write.writeheader() 
          csv_write.writerows(data)


def dir_info(dir_, dir_res):
    res = []

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
            res.append({'object': file,
                        'parent': parent_fold,
                        'type_obj': 'file',
                        'size': size})
            
        # проходимся по дочерним папкам
        # и добавляем их размер в сумму для родительской папки
        # значения берем из созданного словаря
        # 1 позиция - список папок в родительской папке проходимся по ней
        for fold in folder[1]:
            # fold_path = os.path.join(folder[0] ,fold)
            # sum += size_folders[fold_path]
            sum += size_folders[os.path.join(folder[0] ,fold)]

        # добавляем в словарь размер папки
        size_folders[folder[0]] = sum

        # добавляем саму родительскую папку как объект
        parent = folder[0].rsplit("\\", 2)
        res.append({'object': folder[0].rsplit("\\", 1)[-1],
                    'parent': None if len(parent) == 1 else parent[-2],
                    'type_obj': 'folder',
                    'size': sum}) 

    # Запишем результат в файлы разных типов
    name_file = "res1_" + dir_.rsplit("\\", 1)[-1]
    save_data_in_files(res, dir_res, name_file)
    
    

if __name__ == '__main__':
    dir_info("HW_8\\files", "HW_8\\hw_res")
    dir_info("HW_8", "HW_8\\hw_res")


# при большом количестве и глубине папок и файлов, такой код бцдет работать быстрее,
# чем для каждой папки проходится опять по всем папкам и фалам, для подсчета размера папки
# мы используем для этого уже ранее полученную информацию