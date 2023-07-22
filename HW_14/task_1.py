# 📌 Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

from string import ascii_lowercase

def clean_text(text: str) -> str:
    letters = ascii_lowercase + " "
    return "".join([char for char in text.lower() if char in letters])

if __name__ == "__main__":
    text = ""
    print(clean_text("В результате написания тестов получим следующий код: def is_prime(p: int) -> bool:"))
