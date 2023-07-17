import os

from my_exception import MissingFolderException

class Sort_files():
    def __init__(self, dir_, dict_folders):
        if not os.path.exists(dir_): raise MissingFolderException(dir_)
        if len(dict_folders) == 0: raise ValueError(f'The dictionary should not be empty')

        self.__dir_ = dir_
        self.__dict_folders = dict_folders

    def group_files(self):

        os.chdir(self.__dir_ )

        files = [file for file in os.listdir() if os.path.isfile(file)]

        for fold in self.__dict_folders:
            if fold not in os.listdir():
                os.mkdir(fold)

        for file in files:
            for fold, exts in self.__dict_folders.items():
                if file.split('.')[-1] in exts:
                    os.replace(file, os.path.join(fold, file))



if __name__ == '__main__':
    
    dct = {
    'Видео': ('mkv', 'avi', 'mp4'),
    'Изображения' : ('png', 'jpg', 'jpeg'),
    'Текст': ('txt', 'bin', 'pdf', 'docx'),
    'Торенты': ('torrent')
    }

    # sort_my_dir = Sort_files(os.getcwd(), dct)
    # sort_my_dir.group_files()

    # test 1
    sort_my_dir = Sort_files("HW_13\\task", dct)
    sort_my_dir.group_files()

    # test 2
    dct = {}
    sort_my_dir = Sort_files(os.getcwd(), dct)