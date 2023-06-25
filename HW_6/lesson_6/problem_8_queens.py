# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# # 
# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

__all__ = ["check_8_queens", "gen_8_queens", "all_combinations"]

from random import sample

POSITIONS = [(i, j) for i in range(1, 9) for j in range (1, 9)]

def  check_8_queens(arr: list):
    n = len(arr)
    for i in range(n -  1):
        for j in range(i + 1, n):
            if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1]:
                return False
            if abs(arr[i][0] - arr[j][0]) == abs(arr[i][1] - arr[j][1]):
                return False
    return True      

def gen_8_queens():
    return sample(POSITIONS , 8)

def true_8_queens(n = 4):
    positions_lst = []
    i = 0
    while i < n:
        pos = gen_8_queens()
        if check_8_queens(pos):
            positions_lst.append(pos)
            i += 1
    return positions_lst


# всё остальное слишком долго
def all_combinations():

    all_comb = []
    
    for j_1 in range(1, 9):
        el_1 = (1, j_1)
        for j_2 in range(1, 9):
            if j_2 == j_1:
                continue
            el_2 = (2, j_2)
            for j_3 in range(1, 9):
                if j_3 in (j_1, j_2):
                    continue
                el_3 = (3, j_3)
                for j_4 in range(1, 9):
                    if j_4 in (j_1, j_2, j_3):
                        continue
                    el_4 = (4, j_4)
                    for j_5 in range(1, 9):
                        if j_5 in (j_1, j_2, j_3, j_4):
                            continue
                        el_5 = (5, j_5)
                        for j_6 in range(1, 9):
                            if j_6 in (j_1, j_2, j_3, j_4, j_5):
                                continue
                            el_6 = (6, j_6)
                            for j_7 in range(1, 9):
                                if j_7 in (j_1, j_2, j_3, j_4, j_5, j_6):
                                    continue
                                el_7 = (7, j_7)
                                for j_8 in range(1, 9):
                                    if j_8 in (j_1, j_2, j_3, j_4, j_5, j_6, j_7):
                                        continue
                                    el_8 = (8, j_8)
                                    temp = [el_1, el_2, el_3, el_4, el_5, el_6, el_7, el_8]
                                    if check_8_queens(temp):
                                        all_comb.append(temp)


    return all_comb
    



if __name__ == '__main__':
    print(check_8_queens([(1, 6), (2, 4), (3, 2), (4, 8), (5, 5), (6, 7), (7, 1), (8, 3)]))
    print(check_8_queens([(1, 6), (2, 4), (3, 2), (4, 8), (5, 5), (6, 7), (7, 1), (7, 3)]))
    print(gen_8_queens())
    # слишком долго работает =>
    # print(*true_8_queens())

    print(len(all_combinations()))




