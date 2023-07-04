# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# декораторами для сохранения параметров,
# декоратором контроля значений и
# декоратором для многократного запуска.
# Выберите верный порядок декораторов.


from random import randint
from task_4 import param as repeat
from task_2 import deco as control
from task_3 import deco as save_json


@repeat(2)
@save_json
@control
def guess_number(high, num_of_attempts):
    '''Угадай число. Игра'''
    num = randint(1, high)
    attempts = 0
    while attempts < num_of_attempts:
        attempts += 1
        user_num = int(input("Какое число загадано?\n"))
        if user_num == num:
            print("Угадали!")
            return True
        print("Загаданное число больше" if user_num < num else "Загаданное число меньше")
    else:
        print("Вы проиграли")
        print("Было загадано число", num)
        return False

if __name__ == '__main__':
    guess_number(1000, 2)