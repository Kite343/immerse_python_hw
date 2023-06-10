# ✔ Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions
import math

def task_action(n_1, n_2):
    a = n_1[0] * n_2[1] + n_1[1] * n_2[0]
    b = n_1[1] * n_2[1]
    nod = math.gcd(a, b)
    a //= nod
    b //= nod
    if b == 1:
        n_res_1 = str(a)
    else:
        n_res_1 = str(a) + "/" + str(b)
    a = n_1[0] * n_2[0]
    b = n_1[1] * n_2[1]
    nod = math.gcd(a, b)
    a //= nod
    b //= nod
    if b == 1:
        n_res_2 = str(a)
    else:
        n_res_2 = str(a) + "/" + str(b)
    return n_res_1, n_res_2

def input_fracthion_num():
    while True:
        print("Введите дробное число вида a/b (знаменатель не может быть равен 0):")
        num = input()
        if "/" in num:
            num = num.split("/")
            if len(num) == 2 and \
            num[0].isdigit() and num[1].isdigit() and int(num[1]) != 0:
                return  int(num[0]), int(num[1])          

def action():
    while True:
        com = "Выберите действие\n \
            1 - выполнить задачу\n \
            2 - выйти\n"
        choice = input(com)
        if choice.isdigit() and choice in ("1", "2"):
            return choice
        else:
            print("Введите номер нужной операции (это должно быть число)")
        

start = True
while start:
    choice = action()
    match choice:
        case '1':
            print("Введите первое дробное число")
            num_1 = input_fracthion_num()
            print("Введите второе дробное число")
            num_2 = input_fracthion_num()
            
            res = task_action(num_1, num_2)
            print(f"сумма равна {res[0]}")
            print(f"произведение равно {res[1]}")

            print("Проверка суммы")
            chek = fractions.Fraction(num_1[0], num_1[1]) + fractions.Fraction(num_2[0], num_2[1])
            print(f"{res[0] == str(chek)} {chek} = {res[0]}")

            print("Проверка произведения")
            chek = fractions.Fraction(num_1[0], num_1[1]) * fractions.Fraction(num_2[0], num_2[1])
            print(f"{res[1] == str(chek)} {chek} = {res[1]}")

        case '2':
            start = False

