# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

from math import factorial

class Factorial():

    def __init__(self, k) -> None:
        self.history = []
        self._k = k

    def __call__(self, n, *args, **kwds):
        result = factorial(n)
        self.history.append((n, result))
        # if len(self.history) > self.k:
        #     self.history.pop(0)
        self.history = self.history[-self._k:]
        return result
    
    def print_results(self):
        for n, res in self.history:
            print(f"{n}! = {res}")

if __name__ == "__main__":
    calk_fact = Factorial(5)
    print(calk_fact(3))
    print(calk_fact(4))
    print(calk_fact(5))
    print(calk_fact(6))
    print(calk_fact(7))
    print(calk_fact(8))
    calk_fact.print_results()

