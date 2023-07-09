# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

# task_3
# Добавьте к задачам 1 и 2 строки документации для классов.

import time


class My_Str(str):
    """
    Строка имеющая автора и время создания,
    Обладает всеми свойствами строк
    A string that has an author and creation time,
    Has all the properties of strings
    """

    def __new__(cls, string, *args, **kwargs):
        instance = super().__new__(cls, string)
        return instance
    
    def __init__(self, string, name):
        self.string = string
        self.name = name
        self.time = time.time()
    
    def __str__(self):
        return f"{self.string}"
        # return f"Instance of the class {self.__class__.__name__}, name = {self.name}, time = {self.time}, streeng = {self.string}"
        # return f"Instance of the class My_Str, name = {self.name}, time = {self.time}, streeng = {self.string}"
    
    def __repr__(self):
        return f"{type(self).__name__}({self.string}, {self.name})"
        # return f"My_Str({self.string}, {self.name})"

if __name__ == '__main__':
    str_1 = My_Str("test_1", "name_1")
    print(str_1)
    print(str_1.upper())
    time.sleep(1)
    str_2 = My_Str("test_2", "name_2")
    print(str_2)
    print(str_2.upper())
    print(str_1.lower())
    print(str_1.name, str_2.name)
    print(str_2.time - str_1.time)
    # help(My_Str)
    print(repr(str_1))
