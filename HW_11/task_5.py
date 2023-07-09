# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

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
    
    def __add__(self, other):
        new_perimetr = self.perimetr() + other.perimetr()
        a = new_perimetr // 2
        b = new_perimetr - a
        return Rectangle(a, b)

    def __sub__(self, other):
        new_perimetr = abs(self.perimetr() - other.perimetr())
        a = new_perimetr // 2
        b = new_perimetr - a
        return Rectangle(a, b)
    
    def __str__(self):
        return f"Instance of the class {self.__class__.__name__}, length = {self.length}, width = {self.width}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.length}, {self.width})"

if __name__ == '__main__':
    r_1 = Rectangle(6, 3)
    print(r_1.perimetr(), r_1.square())
    r_2 = Rectangle(2, 3)
    print(r_2.perimetr(), r_2.square())
    print(r_1 + r_2)
    print(r_1 - r_2)
    print(repr(r_1))