# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json
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

    def __enter__(self):
        self.__temp = self.history[:]
        # return self.__temp
        return self.history
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # на случай возникновения ошибки, чтобы все осталось как было
        if exc_type is not None:
            self.history = self.__temp[:]

        filename = f"{self.__class__.__name__}.json"
        res = {"results": self.history}
        with open(filename, 'w', encoding='utf-8') as f_j:
            json.dump(res, f_j, ensure_ascii=False, indent=2)

        del  self.__temp

        return False


if __name__ == "__main__":
    calk_fact = Factorial(5)
    with calk_fact as c_f:
        print(calk_fact(3))
        print(calk_fact(4))
        print(calk_fact(5))
        print(calk_fact(6))
        print(calk_fact(7))
        print(calk_fact(8))
    calk_fact.print_results()

    # with calk_fact as c_f:
    #     print(calk_fact(9))
    #     print(calk_fact(-10))
    # calk_fact.print_results()