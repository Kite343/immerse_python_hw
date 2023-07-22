class BaseException(Exception):

    def __init__(self):
        pass

    def __str__(self):
        pass

class SizeException(BaseException):

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"the size cannot be <= 0, your value {self.size} "

class Rectangle:

    def __init__(self, length: int or float, width: int or float = None) -> None:
        if width == None:
            width = length

        if length <= 0: raise SizeException(length)
        if width <= 0: raise SizeException(width)

        self.length = length
        self.width = width

    def perimetr(self):
        return 2 * (self.width + self.length)

    def square(self):
        return self.width * self.length

    def __check_type(self, ob):
        if type(ob) is not  Rectangle:
            raise TypeError(f"object {ob} has the type {type(ob)}\ntype required Rectangle")

    def __add__(self, other):
        self.__check_type(other)
        new_perimetr = self.perimetr() + other.perimetr()
        a = new_perimetr // 2
        b = new_perimetr - a
        return Rectangle(a, b)

    def __sub__(self, other):
        self.__check_type(other)
        new_perimetr = abs(self.perimetr() - other.perimetr())
        a = new_perimetr // 2
        b = new_perimetr - a
        return Rectangle(a, b)

    def __eq__(self, other):
        self.__check_type(other)
        return self.square() == other.square()

    def __gt__(self, other):
        self.__check_type(other)
        return self.square() > other.square()

    def __ge__(self, other):
        self.__check_type(other)
        return self.square() >= other.square()

    def __str__(self):
        return f"Instance of the class {self.__class__.__name__}, length = {self.length}, width = {self.width}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.length}, {self.width})"

if __name__ == '__main__':
    # r_1 = Rectangle(6, 3)
    # print(r_1.perimetr(), r_1.square())
    # r_2 = Rectangle(2, 3)
    # print(r_2.perimetr(), r_2.square())
    # print(r_1)
    # print(repr(r_1))
    # print(r_1 + r_2)
    # print(r_1 - r_2)
    # print(r_1 == r_2)
    # print(r_1 > r_2)
    # print(r_1 < r_2)
    # print(r_1 >= r_2)
    # print(r_1 <= r_2)
    # print(r_1 != r_2)

    # tests exceptions
    # r_1 = Rectangle(6, -3)

    r_1 = Rectangle(6, 3)
    print(r_1 + 2)