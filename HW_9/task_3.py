# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, 
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые 
# аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
import os
from functools import wraps


def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        filename = "files/" + func.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f_j:
                list_file = json.load(f_j)
        else:
            list_file = []
        result = func(*args, **kwargs)
        list_file.append({
            'args': (args, kwargs),
            'result': result
        })
        with open(filename, 'w', encoding='utf-8') as f_j:
            json.dump(list_file, f_j, indent=1)
        return result
    return wrapper

@deco
def get_any(num, *args, **kwargs):
    return num

@deco
def qwerty(q):
    print(q)

@deco
def funk(**kwargs):
    return([*kwargs.values()])
    # return(str(kwargs.values()))

if __name__ == '__main__':
    my_dict = {1:1, 2:2}
    print(get_any(1, 11, 22, 33, my_dict))
    print()
    qwerty("stop")
    print()
    print(get_any(13, a=7, n=9))
    print()
    print(funk(q=1, h=3))
    
