# * Создайте класс прямоугольник.
# * Класс должен принимать длину и ширину при создании
# экземпляра.
# * У класса должно быть два метода, возвращающие периметр
# и площадь.
# * Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат

class Rectangle:

    def __init__(self, length, width=None):
        if width == None:
            width = length

        self.length = length
        self.width = width
    
    def perimetr(self):
        return 2 * (self.width + self.length)
    
    def square(self):
        return self.width * self.length
    
if __name__ == '__main__':
    r_1 = Rectangle(2, 3)
    print(r_1.perimetr(), r_1.square())