# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

from math import factorial 

class Gen_Factorial:
    def __init__(self, start, stop = None, step = 1):
        if stop is None:
            start, stop = 1, start
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            res = factorial(self.start)
            self.start += self.step
            return res
        raise StopIteration

if __name__ == "__main__":
    gen = Gen_Factorial(1, 10, 2)
    for num in gen:
        print(num)
    