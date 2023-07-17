# 📌 Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

# task 6
# 📌 Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# 📌 Передавайте необходимые данные из основного кода
# проекта.

class BaseException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        pass

class AccessException(BaseException):
    def __init__(self, user_id):
        self.user_id = user_id
    def __str__(self):
        return f"the user id {self.user_id} is missing "

class LevelException(BaseException):
    def __init__(self, level, name):
        self.level = level
        self.name = name
    def __str__(self):
        return f"{self.name} have level {self.level}, cannot be added"