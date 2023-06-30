#  ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

__all__ = ["task_2"]

from random import randint, choice, sample, shuffle


VOVELS = "aeiouy"
CONSONANT = "qwrtpsdfghjklzxcvbnm"
MIN_LEN = 4
MAX_LEN =7

def name_create(len):
    name = []
    name.append(choice(VOVELS))
    name.append(choice(CONSONANT))
    name += sample(VOVELS + CONSONANT, len - 2)
    shuffle(name)
    return ''.join(name)


def task_2(count_names, filename):
    with open(filename, 'a', encoding="utf-8") as f:
        for _ in range(count_names):
            f.write(f"{name_create(randint(MIN_LEN, MAX_LEN))}\n")

if __name__ == '__main__':
    filename = "HW_7\\files\\names.txt"
    task_2(5, filename)