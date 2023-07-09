# * Создайте функцию-замыкание, которая принимает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# * Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint

def make(high, num_of_attempts):
    def guess_number():
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
    return guess_number


if __name__ == '__main__':
    high = 100
    num_of_attempts = 5
    res = make(high, num_of_attempts)
    res()
    res()