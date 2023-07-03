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
            
        # проходимся по уже записанным объектам
        # и добавляем в сумму размеры папок для которых данная папка является родительской
        # лучше пока не придумала, вероятно можно использовать словарь для уменьшения количества операций
        # 1 позиция - список папок в родительской папке проходимся по ней
        for fold in folder[1]:
            for obj in res:
                # если объект из записанных имеет тоже имя, что и дочерняя папка
                # и родителем является рассматриваемая папка (на случай одинаковых имен папок в разных папках)
                #  то добавляем её размер в сумму
                if obj['object'] == fold and obj['parent'] == folder[0]:
                    sum += obj['size']

        # добавляем саму родительскую папку как объект
        # в качестве родительской папки записываем весь путь,
        # чтобы при подсчете размера папки (выше код)
        # исключить папки находящиеся в разных папках, но имеющих одинковые названия и подпапки
        parent = folder[0].rsplit("\\", 1)
        res.append({'object': folder[0].rsplit("\\", 1)[-1],
                    'parent': None if len(parent) == 1 else parent[-2],
                    'type_obj': 'folder',
                    'size': sum}) 
    
    # оставим только имя родительской папки у папок (почистим)
    for obj in res:
        if obj['type_obj'] == 'folder' and obj['parent']:
            obj['parent'] = obj['parent'].rsplit("\\", 1)[-1]

    # Запишем результат в файлы разных типов
    name_file = "res1_" + dir_.rsplit("\\", 1)[-1]
    save_data_in_files(res, dir_res, name_file)
    
    

if __name__ == '__main__':
    dir_info("HW_8\\files", "HW_8\\hw_res")
    dir_info("HW_8", "HW_8\\hw_res")


# при большом количестве и глубине папок и файлов, такой код бцдет работать быстрее,
# чем для каждой папки проходится опять по всем папкам и фалам, для подсчета размера папки
# мы используем для этого уже ранее полученную информацию