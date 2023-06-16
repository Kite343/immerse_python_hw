# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [2, 3, 4, 5, 8, 2, 4, 5, 5, 0, 1]
#  var1
my_list = [i for i in my_list if my_list.count(i) != 2]
print(my_list)

# var2
del_dict = dict()
for el in my_list:
    del_dict[el] = del_dict.get(el, 0) + 1

my_list = [i for i in my_list \
           if i not in [key for key, value in del_dict.items() if value == 2]]
print(my_list)