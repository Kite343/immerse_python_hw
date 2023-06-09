# 4
# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
# 5
# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
# 6
# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). 
# Функция формирует словарь с информацией о результатах отгадывания. 
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
# Для формирования результатов используйте генераторное выражение.

__all__ = ["riddle_box", "riddle_game"]

def riddles_res_add(riddle: str, num: int):
    _riddles_res[riddle] = num

def print_res():
    print(*(f"Загадка: {k}\nотгадана с {v} попыток" for k,v in _riddles_res.items()), sep="\n")

def riddle_game(riddle: str, answers: list, attempts=3):
    print(riddle)
    print(f"Количество ваших попыток: {attempts} ")
    count = 1
    while count <= attempts:
        user_answer = input("Ваш вариант ответа?\n")
        if user_answer.lower() in answers:
            print(f"Угадали!\nС попытки номер:{count}")
            return count
        count += 1
        print("Неверно")
    else:
        print("Вы проиграли")
        print("Варианты ответа:", *answers)
        return 0

def riddle_box():
    box = {
        "Что принадлежит вам, но другие используют это чаще?": ["имя", "name"],
        "Не огонь, а жжется.": ["крапива"],
        "На верхушке стебелька солнышко и облака.": ["ромашка"],
        "Что всегда перед нами, но мы его не видим?": ["будущее"],
        "Что может жить на бумаге, но умрёт в воде?": ["огонь", "пламя"]
    }

    for k, v in box.items():
       riddles_res_add(k, riddle_game(k, v))

_riddles_res = dict()

if __name__ == '__main__':
    riddle_box()
    print_res()