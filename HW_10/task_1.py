# * Создайте класс окружность.
# * Класс должен принимать радиус окружности при создании
# экземпляра.
# * У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math

class Circle():

    def __init__(self, r):
        self.radius = r

    def len_circle(self):
        return 2 * math.pi * self.radius
    
    def area_circle(self):
        return math.pi * self.radius ** 2
    
if __name__ == '__main__':
    c_1 = Circle(10)
    print(c_1.len_circle(), c_1.area_circle())