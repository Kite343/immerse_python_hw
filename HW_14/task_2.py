# 📌 Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# 📌 1. возврат строки без изменений
# 📌 2. возврат строки с преобразованием регистра без потери
# символов
# 📌 3. возврат строки с удалением знаков пунктуации
# 📌 4. возврат строки с удалением букв других алфавитов
# 📌 5. возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_lowercase

def clean_text(text: str) -> str:
    """
    удаляет из текста все символы кроме букв латинского алфавита и пробелов.
    Возвращается строка в нижнем регистре.

    >>> clean_text("text str")
    'text str'
    >>> clean_text("PytHoN")
    'python'
    >>> clean_text("(text: str) -> str")
    'text str  str'
    >>> clean_text("python не питон")
    'python  '
    >>> clean_text("pYthOn, не питон!!!")
    'python  '
    """
    letters = ascii_lowercase + " "
    return "".join([char for char in text.lower() if char in letters])

if __name__ == "__main__":
    # text = ""
    # print(clean_text("В результате написания тестов получим следующий код: def is_prime(p: int) -> bool:"))
    import doctest
    doctest.testmod(verbose=True)