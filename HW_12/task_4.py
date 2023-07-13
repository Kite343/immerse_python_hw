# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.
# task 5
# 📌 Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

class Rectangle:

    __slots__ = ("_length", "_width")

    def __init__(self, length, width=None):
        if width == None:
            width = length

        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, l):
        if l > 0:
            self._length = l

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, w):
        if w > 0:
            self._width = w

    def perimetr(self):
        return 2 * (self._width + self._length)

    def square(self):
        return self._width * self._length

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

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __str__(self):
        return f"Instance of the class {self.__class__.__name__}, length = {self._length}, width = {self._width}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._length}, {self._width})"

if __name__ == '__main__':
    r_1 = Rectangle(6, 3)
    print(r_1.perimetr(), r_1.square())
    r_2 = Rectangle(2, 3)
    print(r_2.perimetr(), r_2.square())
    print(r_1)
    print(repr(r_1))
    print(r_1 + r_2)
    print(r_1 - r_2)
    print(r_1 == r_2)
    print(r_1 > r_2)
    print(r_1 < r_2)
    print(r_1 >= r_2)
    print(r_1 <= r_2)
    print(r_1 != r_2)
    print()
    print(r_1.length)
    r_1.length = 2
    print(r_1.length)
    print()
    print(r_2.width)
    r_2.width = -4
    print(r_2.width)
    r_2.width = 4
    print(r_2.width)
    print()
    # r_3 = Rectangle(-6, 3)
    # print(r_3.perimetr(), r_3.square())
    
    print(Rectangle.__dict__)
    print(r_1.__dict__)