# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json
from math import factorial

class Factorial():

    def __init__(self, k=10) -> None:
        self.history = []
        self._k = k

    def __call__(self, n, *args, **kwds):
        result = factorial(n)
        self.history.append({n: result})
        self.history = self.history[-self._k:]
        return result
    
    def print_results(self):
        for res in self.history:
            for k, v in res.items():
                print(f"{k}! = {v}")

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        filename = f"{self.__class__.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as f_j:
            json.dump(self.history, f_j, ensure_ascii=False, indent=2)


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