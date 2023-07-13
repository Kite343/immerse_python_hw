# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv

class Subjects:
    """Класс хранит предметы и оценки по ним"""
    __MIN_GRADE = 2
    __MAX_GRADE = 5
    __MIN_TEST_GRADE = 0
    __MAX_TEST_GRADE = 100
    
    def __init__(self, subjects_file):
        """Создает объект, предметы берутся из файла"""
        self.subjects = self.__create_dict(subjects_file)

    def __create_dict(self, file):
        sub = {}
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                for s in row:
                    sub[s] = {"grades": [],
                            "tests": []}          
        return sub
    
    @classmethod
    def validate(cls, value, min, max):
        if type(value) != int or value < min or value > max:
            raise TypeError(f"Значение должно быть целым числом в диапазоне [{min}; {max}]")
        
    def add_grade(self, subject, grade):
        """Добавление оценки по предмету"""
        self.validate(grade, self.__MIN_GRADE, self.__MAX_GRADE)
        self.subjects[subject]["grades"].append(grade)

    def add_test(self, subject, grade):
        """Добавление оценки за тест"""
        self.validate(grade, self.__MIN_TEST_GRADE, self.__MAX_TEST_GRADE)
        self.subjects[subject]["tests"].append(grade)

    def average_grade_tests(self):
        """Средняя оценка за тесты по каждому предмету"""
        tests = {}
        for k, v in self.subjects.items():
            value = round(sum(v["tests"]) / len(v["tests"]), 1)
            tests[k] = value
        # вероятно лучше делать возврат словаря
        # как временный вариант печать в функции
        for k, v in tests.items():
            print(f"{k} средний бал по тестам: {v}")

    def average_grade(self):
        """Общий средний балл по всем предметам"""
        res = []
        for v in self.subjects.values():
            res.extend(v["grades"])
        return round(sum(res) / len(res), 1)
        #     a_g = round(sum(res) / len(res), 1)
        # print(f"общий средний бал по всем предметам: {a_g}")
        
        
    def get_subjects_lst(self):
        """список предметов"""
        return list(self.subjects.keys())
    
    def get_subject_tests(self, subject):
        """оценки за тесты по предмету"""
        return self.subjects[subject]["tests"]
    
    def get_subject_grades(self, subject):
        """оценки по предмету"""
        return self.subjects[subject]["grades"]
    


if __name__ == "__main__":
    s_1 = Subjects("HW_12\\subjects.csv")
    print(s_1.get_subjects_lst())
    s_1.add_grade('math', 5)
    print(s_1.get_subject_grades('math'))
    s_1.add_test('math', 88)
    print(s_1.get_subject_tests('math'))
    # s_1.add_test('math', 103)

