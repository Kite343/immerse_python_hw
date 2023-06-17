# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def gen_fibonacci(n: int):
    fib_1, fib_2 = 0, 1
    for i in range(n):
        if i == 0:
            yield fib_1
        elif i == 1:
            yield fib_2
        else:
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            yield fib_2

print(*gen_fibonacci(5)) # 0, 1, 1, 2, 3
print()
print(*gen_fibonacci(10)) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34