# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = "Ivan"
next = 6
tigers = "White"
dogs = "Rex"
mute = 7
ENDSWITH_STR = 's'

def changing_variable_names():
    glob = globals()
    print(glob)
    print()
    for key in tuple(glob.keys()):
        if key.endswith(ENDSWITH_STR):
            temp = glob[key]
            glob[key] = None
            glob[key[: -1]] = temp
    print(glob)


changing_variable_names()
print()
print("check")
print()
print(names, name)
print(tigers, tiger)
print(dogs, dog)
