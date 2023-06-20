# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

line_test = "C:\\Users\\Kat\\Desktop\\Kite GB\\temp\\test.docx"

def file_info(line):
    point = line.rfind(".")
    slash = line.rfind("\\")
    return (line[: slash + 1], line[slash + 1: point], line[point:])

print(file_info(line_test))