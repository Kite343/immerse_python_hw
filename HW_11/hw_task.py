# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix():

    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    def print(self):
        print("\n".join([" ".join(map(str, i)) for i in self.matrix]))

    def size(self):
        size = (len(self.matrix), len(self.matrix[0]))
        return size

    def __add__(self, other):
        if self.size() != other.size():
            print('Нельзя складывать матрицы таких размерностей')
            return None
        else:
            row = len(self.matrix)
            col = len(self.matrix[0])
            result_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(col)] for i in range(row)]
            return Matrix(result_matrix)


    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.matrix]
            return Matrix(result)
        elif len(self.matrix[0]) != len(other.matrix):
            print('Нельзя перемножить матрицы таких размерностей')
            return None
        else:
            row_self = len(self.matrix)
            colum_self = len(self.matrix[0])
            colum_other = len(other.matrix[0])
            result_matrix = [[0 for j in range(colum_other)] for i in range(row_self)]
            for i in range(row_self):
                for j in range(colum_other):
                    for q in range(colum_self):
                        result_matrix[i][j] += self.matrix[i][q] * other.matrix[q][j]
            return Matrix(result_matrix)
        
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other) -> bool:
        return self.matrix == other.matrix

    def __str__(self):
        return f"Instance of the class {self.__class__.__name__}, matrix = {self.matrix}"
        # return f"Instance of the class Matrix, matrix = {self.matrix}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.matrix})"
        # return f"{type(self).__name__}(self.matrix)"
        # return f"Matrix(self.matrix)"

if __name__ == '__main__':
    a = Matrix([[1, 2, 3], [1, 2, 3]])
    print(a)
    print(repr(a))
    print()
    a.print()
    print()
    print(f"a size = {a.size()}")
    print()

    print("c = a * 3")
    c = a * 3
    c.print()
    print()

    print("d = 3 * a")
    d = 3 * a
    print(d)
    print()

    print("a + d")
    print(a + d)
    print()

    b = Matrix([[2, 1], [2, 1], [2, 1]])
    print("a + b")
    print(a + b)
    print()
    print("a * b")
    e = a * b
    print(e)
    print()

    print("b * a")
    b = Matrix([[2, 1], [2, 1], [2, 1]])
    e = b * a
    print(e)
    print()

    m = Matrix([[1, 2]])
    print(a * m)
    print()

    print("c == d")
    print(c == d)
    print("a == c")
    print(a == c)