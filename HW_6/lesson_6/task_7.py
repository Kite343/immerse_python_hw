# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.
from sys import argv

__all__ = ["date_chek"]

def _chek_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def date_chek(date_: str):
    d, m, y = map(int, date_.split("."))
    if d < 1 or d > 31 or m < 1 or m > 12 or y < 1 or y > 9999:
        return False
    if m in (4, 6, 9, 11) and d > 30:
        return False
    if m == 2 and (d > 29 or not _chek_leap(y) and d > 28):
        return False
    return True

if __name__ == '__main__':
    # print(date_chek(input()))
    # print(date_chek("22.16.5098"))
    # print(date_chek("31.04.5098"))
    # print(date_chek("29.02.2000"))
    # print(date_chek("29.02.2001"))
    # print(date_chek("28.02.2001"))
    print(date_chek(argv[1]))