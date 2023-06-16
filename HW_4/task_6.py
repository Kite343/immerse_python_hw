# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# Для простоты будем использовать только положительную индексацию

def sum_nums_range(nums: list, a: int, b: int):
    n = len(nums)
    if a < 0:
        if abs(a) > n:
            a = 0
        else:
            a += n
    if b < 0:
        if abs(b) > n:
            b = 0
        else:
            b += n
    if a > b:
        a, b = b, a
    return sum(nums[a if a >= 0 else 0: b + 1 if b < n else n])
    

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(sum_nums_range(numbers, 1, 5))        # 15
print(sum_nums_range(numbers, 5, 1))        # 15
print(sum_nums_range(numbers, 0, 12))       # 45
print(sum_nums_range(numbers, -9, -1))      # 45
print(sum_nums_range(numbers, -1, -9))      # 45
print(sum_nums_range(numbers, -20, -1))     # 45
print(sum_nums_range(numbers, -1, -20))     # 45
print(sum_nums_range(numbers, 0, -20))      # 0