# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.

def my_get(dct, key, default):
    try:
        return dct[key]
    except KeyError:
        return default
    
if __name__ == "__main__":
    d = {
        1: "a",
        2: "b",
        3: "c",
        4: "d"
    }

    print(my_get(d, 1, -1))
    print(my_get(d, 0, -1))
    print(my_get(d, 3, -1))
    print(my_get(d, "f", -1))
