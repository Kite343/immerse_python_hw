# ✔ Напишите функцию для транспонирования матрицы

def transposed_matrix(matrix: list):
    len_i = len(matrix)
    len_j = len(matrix[0])
    return [[matrix[i][j] for i in range(len_i)] for j in range(len_j)]

def print_matrix(matrix):
    len_i = len(matrix)
    len_j = len(matrix[0])
    n = max([len(str(matrix[i][j])) for i in range(len_i) for j in range(len_j)]) + 1
    for i in range(len_i):
        for j in range(len_j):
            # print(str(matrix[i][j]).ljust(n), end=' ')
            print(f"{matrix[i][j]:>{n}}", end=' ')
        print()

matrix_1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 0, 0]
]

print_matrix(matrix_1)
print()
print_matrix(transposed_matrix(matrix_1))
print()
print_matrix(matrix_2)
print()
print_matrix(transposed_matrix(matrix_2))
print()