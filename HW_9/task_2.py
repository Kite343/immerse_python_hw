# * Дорабатываем задачу 1.
# * Превратите внешнюю функцию в декоратор.
# * Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# * Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from random import randint
from functools import wraps


def deco(func):
    @wraps(func)
    def wrapper(number, num_of_attempts):
        if not 1 <= number <= 100:
            print(f'Параметр {number = } не в диапазоне')
            number = randint(1, 100)
            print(f'Параметр изменен на {number}')
        if not 1 <= num_of_attempts <= 10:
            print(f'Параметр {num_of_attempts = } не в диапазоне')
            num_of_attempts = randint(1, 10)
            print(f'Параметр изменен на {num_of_attempts}')
        return func(number, num_of_attempts)
    return wrapper


# @deco
def guess_number(high, num_of_attempts):
    num = randint(1, high)
    attempts = 0
    while attempts < num_of_attempts:
        attempts += 1
        user_num = int(input("Какое число загадано?\n"))
        if user_num == num:
            print("Угадали!")
            return
        print("Загаданное число больше" if user_num < num else "Загаданное число меньше")
    else:
        print("Вы проиграли")
        print("Было загадано число", num)



if __name__ == '__main__':
    number = 108
    num_of_attempts = 5
    guess_number = deco(guess_number)
    guess_number(number, num_of_attempts)