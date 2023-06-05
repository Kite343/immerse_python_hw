# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

def guess_number():
    num = randint(0, 1000)
    attempts = 10
    while attempts > 0:
        user_num = int(input("Какое число загадано?\n"))
        if user_num == num:
            print("Угадали!")
            return
        attempts -= 1
        print("Загаданное число больше" if user_num < num else "Загаданное число меньше")
    else:
        print("Вы проиграли")
        print("Было загадано число", num)

guess_number()