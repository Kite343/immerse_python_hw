# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

def drawing_christmas_tree(size):
    whitespace = size - 1
    stars = "*"
    for i in range(0, size):
        print(" " * whitespace + stars)
        whitespace -= 1
        stars = stars + "**"


drawing_christmas_tree(int(input("Введите высоту ёлки: ")))