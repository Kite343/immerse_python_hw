# 📌 Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import json
from string import ascii_letters
from subjects import Subjects
from random import randint


class Descript_name:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.verify_fio(value)
        setattr(instance, self.param_name, value)

    @classmethod   
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        
        if not fio.istitle():
            raise TypeError("ФИО должны быть написаны с заглавной буквы")
 
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи ФИО")
 
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")
            

class Student(Subjects):
    fio = Descript_name()
    def __init__(self, fio, *args, **kwargs):
        self.fio = fio
        super().__init__(*args, **kwargs)

    def rating_log(self):
        file_json = f'{self.fio}.json'
        with open(file_json, 'w', encoding='utf-8') as f:
            json.dump(self.subjects, f, ensure_ascii=False, indent=1)
        


if __name__ == "__main__":
    student_1 = Student("Ivanov Ivan Ivanovich", "HW_12\\subjects.csv")
    print(student_1.fio)
    print(*student_1.get_subjects_lst(), sep=", ")
    # student_1.add_grade('math', 5)
    # student_1.add_grade('math', 4)
    # print(*student_1.get_subject_grades('math'), sep=", ")
    print()
    for s in student_1.get_subjects_lst():
        for _ in range(randint(6, 12)):
            student_1.add_grade(s, randint(2, 5))
            student_1.add_test(s, randint(0, 100))
        print(s)
        print("оценки")
        print(*student_1.get_subject_grades(s), sep=", ")
        print("тесты")
        print(*student_1.get_subject_tests(s), sep=", ")
        print()
    
    student_1.average_grade_tests()
    print()
    print(student_1.average_grade())
    print("Общий средний балл по всем предметам")
    student_1.rating_log()
    

    student_2 = Student("Ivanov-Sidorov Ivan Ivanovich", "HW_12\\subjects.csv")

    # (тест) выдают ошибки:
    # student_3 = Student("Ivanov ivan iVanovich", "HW_12\\subjects.csv")
    # student_4 = Student("Ivanov Ivan", "HW_12\\subjects.csv")
    # student_5 = Student("Ivanov@ Ivan Ivanovich", "HW_12\\subjects.csv")
    # student_4 = Student(6, "HW_12\\subjects.csv")

