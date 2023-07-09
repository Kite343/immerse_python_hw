# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел 
# из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import os
from random import randint
from functools import wraps

def decor_write_json(dir_):
    '''запись в json файл'''
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            file_json = f'{dir_}\\{func.__name__}.json'
            with open(file_json, 'w', encoding='utf-8') as f:
                json.dump(res, f, ensure_ascii=False, indent=1)
            return res
        return wrapper
    return deco

def decor_read_csv_in_func(file):
    '''чтение данных из csv файла и передача в функцию'''
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            with open(file, 'r', encoding='utf-8', newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    # print(*row)
                    a, b, c = map(int, row[0].split())
                    res = func(a, b, c)
                    results.append({
                        "params": (a, b, c),
                        "result": res
                    })
            return(results)
        return wrapper
    return deco


@decor_write_json(os.getcwd())
@decor_read_csv_in_func(f"{os.getcwd()}\\random_nums.csv")
# def quadratic_equation(a=1, b=1, c=1):
def quadratic_equation(*args):
    a, b, c = args
    '''Нахождение корней квадратного уравнения'''
    d = b**2 - 4 * a * c
    if d > 0:
        x_1 = (-b + d**0.5) / 2 * a
        x_2 = (-b - d**0.5) / 2 * a
        return x_1, x_2
    elif d == 0:
        x = - b / (2 * a)
        return x
    else:
        return 'Нет корней'

def gen_nums_csv(dir_, n_min=-100, n_max=100):
    '''Генерация csv файла с тремя случайными числами в каждой строке'''
    nums_lines = randint(100,1001)
    with open(dir_ + '\\random_nums.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file,  delimiter=' ')
        for _ in range(nums_lines):
            a = randint(n_min, n_max)
            b = randint(n_min, n_max)
            c = randint(n_min, n_max)
            writer.writerow([a, b, c])   

if __name__ == '__main__':
    gen_nums_csv(os.getcwd())
    # print(quadratic_equation())
    quadratic_equation()

