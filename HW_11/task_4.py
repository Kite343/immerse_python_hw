# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive():
    """
    Archive
    Экземпляры класса хранят числовое и строковое значение
    Класс хранит списки со всеми созданными значениями
    Instances of the class store numeric and string values
    The class stores lists with all created values
    """
    num_lst = []
    str_lst = []
    
    def __init__(self, num, string):
        """
        Added the num parameter,
        Added the string parameter,
        Added num and string in Archive list
        """
        self.num = num
        self.string = string
        self.num_lst.append(num)
        self.str_lst.append(string)

    def __str__(self):
        return f"Instance of the class {self.__class__.__name__}, num = {self.num}, string = {self.string}"
        # return f"Instance of the class Archive, num = {self.num}, string = {self.string}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.num}, {self.string})"
        # return f"{type(self).__name__}({self.num}, {self.string})"
        # return f"Archive({self.num}, {self.string})"

if __name__ == '__main__':
    test_1 = Archive(1, "one")
    test_2 = Archive(2, "two")
    print(test_1.num, test_1.string)
    print(test_2.num, test_2.string)
    print(Archive.num_lst)
    print(Archive.str_lst)
    print(test_1.num_lst)
    print(test_2.str_lst)
    print(test_1)
    print(repr(test_1))
    print(f"{test_2 = }")