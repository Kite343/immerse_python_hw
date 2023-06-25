# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

__all__ = ["group_files"]

import os


DCT = {
    'Видео': ('mkv', 'avi', 'mp4'),
    'Изображения' : ('png', 'jpg', 'jpeg'),
    'Текст': ('txt', 'bin', 'pdf', 'docx'),
    'Торенты': ('torrent')
    }

def group_files(dir_):
    
    os.chdir(dir_)
    
    files = [file for file in os.listdir() if os.path.isfile(file)]

    for fold in DCT:
        if fold not in os.listdir():
            os.mkdir(fold)

    for file in files:
        for fold, exts in DCT.items():
            if file.split('.')[-1] in exts:
                os.replace(file, os.path.join(fold, file))



if __name__ == '__main__':
    # group_files(os.getcwd())
    group_files("HW_7\\files\\task_5")
    
    
