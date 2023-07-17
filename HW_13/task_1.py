# 📌 Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

# def number():
#     while True:
#         try:
#             n = float(input())
#             return n
#         except:
#             print("введено не число")

# def number():
#     while True:
#         n = input("Введите целое или вещественное число: ")
#         try:
#             n = int(n)
#             return n
#         except ValueError as e:
#             print(e)
#             print("введено не целое число")

#         try:
#             n = float(n)
#             return n
#         except ValueError as e:
#             print(e)
#             print("введено не число")

def number():
    while True:
        temp = input("Введите целое или вещественное число: ")
        try:
            n = float(temp)
            if int(n) == n and len(temp.split(".")) == 1:
                n = int(n)
            return n
        except ValueError as e:
            print(e)
            print("введено не число")


if __name__ == "__main__":
    print(number())
    
