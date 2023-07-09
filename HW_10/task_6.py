# task 5
# * Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# * У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# * Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
# task 6
# * Доработайте задачу 5.
# * Вынесите общие свойства и методы классов в класс
# Животное.
# * Остальные классы наследуйте от него.
# * Убедитесь, что в созданные ранее классы внесены правки.

class Animals():
    def __init__(self, name, age, weight):
        self.name = name
        self.weight = weight
        self.age = age

class Fish(Animals):
    def __init__(self, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deep = deep

    def type_deep(self):
        if self.deep <= 3:
            return f"Мелководная"
        elif self.deep < 20:
            return f"Среднеглубинная"
        return f"Глубоководная"

class Dog(Animals):
    def __init__(self, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = height

    def type_size(self):
        if self.height <= 28:
            return f"Ммаленькая"
        elif 3 < self.height < 60:
            return f"Средняя"
        return f"Крупная"
    
class Birds(Animals):

    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_lengh = self.wingspan * 0.45
        return wing_lengh

if __name__ == '__main__':
    Dori = Fish(15, "Dori", 10, 100)
    print(Dori.type_deep())
    Rex = Dog(70, "Rex", 24, 70000)
    print(Rex.type_size())
    Lori = Birds(100, "Lori", 18, 25000)
    print(Lori.specific())