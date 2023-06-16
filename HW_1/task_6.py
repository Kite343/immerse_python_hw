# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

def leap_year_bool(year):
    YEAR_ENTRY_CALENDAR = 1582

    if year < YEAR_ENTRY_CALENDAR:
        return False
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input("Введите год: "))
print("Год високосный" if leap_year_bool(year) else "Год обычный")

