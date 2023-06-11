# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

my_list = [2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 8, 9, 11, 11]

my_dict = dict()
for el in my_list:
    my_dict[el] = my_dict.get(el, 0) + 1

new_list = [key for key, value in my_dict.items() if value > 1]
print(new_list)