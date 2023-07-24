# 📌 На семинаре про декораторы  был создан логирующий
# декоратор (9.3). Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging

logging.basicConfig(filename='task_2.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Аргументы функции {func.__name__} {args}, {kwargs}, результат {result}')
        return result

    return wrapper


@log
def func(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return ((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))


if __name__ == '__main__':
    a = 1
    b = 8
    c = 3
    print(func(a, b, c))