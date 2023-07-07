# * Создайте класс Сотрудник.
# * Воспользуйтесь классом человека из прошлого задания.
# * У сотрудника должен быть:
#     ○ шестизначный идентификационный номер
#     ○ уровень доступа вычисляемый как остаток от деления
#       суммы цифр id на семь

import random
from task_3 import Human

class Personnel(Human):
    __MAG = 7
    __LEN_ID = 6

    def __init__(self, id_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_num = self.__chek_id_num(id_num)
        self.level = self.__level_gen()

    def __level_gen(self):
        return sum(map(int, list(str(self.id_num)))) % self.__MAG

    def __chek_id_num(self, id_num):
        if id_num < 10**(self.__LEN_ID - 1) or id_num >= 10**(self.__LEN_ID):
            id_num = random.randint(10**(self.__LEN_ID - 1), 10**(self.__LEN_ID))
        return id_num


if __name__ == '__main__':
    Anna = Personnel(1234, 23, "Ivanova", "Anna", "Ivanovna")
    print(Anna.full_name())
    print(Anna.get_age())
    Anna.birthday()
    Anna.birthday()
    print(Anna.get_age())
    print(Anna.id_num)