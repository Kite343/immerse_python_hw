# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

from task_2 import Factorial

class Gen_factorial():
    def __init__(self, start, stop = None, step = 1):
        if stop is None:
            start, stop = 1, start
        self.start = start
        self.stop = stop
        self.step = step
        self.f = Factorial((self.stop - self.start + 2) // self.step)
        self.__first = start

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.__first <= self.stop:
            res = self.f(self.__first)
            self.__first += self.step
            return res
        self.__first = self.start # можно будет заново использовать
        raise StopIteration
    
if __name__ == "__main__":
    gen_f = Gen_factorial(1, 11, 2)
    for i in gen_f:
        print(i)

    for i in gen_f:
        print(i)

    print(gen_f.f.history)
    gen_f.f.print_results()
    


    