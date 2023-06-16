# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def num_in_range(first=1, final=999):
    while True:
        data = input("Введите число от 1 до 999: \n")
        if data.isdigit():
            data = int(data)
            if first <= data <= final:
                return data
            
def task(num):
    num_len = len(str(num))
    if num_len == 1:
        print("Введена цифра, её квадрат равен", num**2)
    if num_len == 2:
        print("введено двузначное число, произведение его цифр равно", (num // 10) * (num % 10))
    if num_len == 3:
        print("введено трёхзначное число, его зеркальное отображение", int(str(num)[::-1]))

task(num_in_range())