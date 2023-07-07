# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

import task_6

class Animals_factory:
    dict_type_animal = {
        "Fish": task_6.Fish,
        "Dog": task_6.Dog,
        "Birds": task_6.Birds
    }

    def __init__(self, type_animal, *args, **kwargs):
        self.animal = self.dict_type_animal[type_animal](*args, **kwargs)

if __name__ == '__main__':
    Dori = Animals_factory("Fish", 15, "Dori", 10, 100)
    print(Dori.animal.type_deep())
    Dori = Dori.animal
    print(Dori.type_deep())
    Dori = Animals_factory("Fish", 15, "Dori", 10, 100).animal
    print(Dori.type_deep())
    Rex = Animals_factory("Dog", 70, "Rex", 24, 70000)
    print(Rex.animal.type_size())
    Lori = Animals_factory("Birds", 100, "Lori", 18, 25000)
    print(Lori.animal.specific())