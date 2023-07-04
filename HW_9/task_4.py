# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

from functools import wraps

COUNT = 3

def param(count):
    def deco(func):
        res_list= []
        @wraps(func)
        def wrapper(*args):
            for _ in range(count):
                res = func(*args)
                res_list.append(res)
            return res
        return wrapper
    return deco

# @param(COUNT)
def my_func(*args):
    return(args)

if __name__ == '__main__':
    print(my_func('Hello, World!'))
    print(my_func('Hello, World!'))
    my_func_1 = param(2)(my_func)
    print(my_func_1('Hello, World!'))