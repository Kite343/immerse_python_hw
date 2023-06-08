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
    n_res = (a // nod, b // nod)
    return n_res

def input_fracthion_num():
    print("Введите числитель")
    a = input_num()
    print("Введите знаменатель")
    b = input_num()
    return (a, b)

def input_num():
    while True:
        num = input()
        if num.isdigit():
            return int(num)
        print("Введите целое число")

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
            res_str = str(res[0]) + "/" + str(res[1])
            print(res_str)
            print("Проверка")
            chek = fractions.Fraction(num_1[0], num_1[1]) + fractions.Fraction(num_2[0], num_2[1])
            print(f"{res_str == str(chek)} {chek} = {res_str}")
        case '2':
            start = False
