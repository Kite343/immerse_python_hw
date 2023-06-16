# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

# *Верните все возможные варианты комплектации рюкзака

# расширенный список
# my_things = {
#     "спальник": 1000, "палатка": 4000,
#     "табурет": 500, "кружка": 200,
#     "тарелка": 200, "макароны": 800,
#     "колбаса": 1000, "тушенка": 500,
#     "картошка": 2500, "гречка": 1500,
#     "ведро": 600, "топор": 1600,
#     "пила": 1200, "запасная одежда": 1400,
#     "резиновые сапоги": 600, "куртка": 700,
#     "аптечка": 400, "книга": 300,
# }

# решение с модулем выдает больше вариантов
from itertools import combinations


my_things = {
    "спальник": 1000, "палатка": 4000,
    "табурет": 500, "кружка": 200,
    "тарелка": 200, "макароны": 800,
    "колбаса": 1000, "тушенка": 500,
    "картошка": 2500, "гречка": 1500,
    "ведро": 600, "топор": 1600,
}

print("Вес всех вещей")
print(sum(my_things.values()))

weight = int(input("Введите грузоподъемность рюкзака в граммах\n"))

things_name = [*my_things.keys()]
variants = []
for n in range(1, len(things_name) + 1):
    temp_compinats = combinations(things_name, n)
    for var in temp_compinats:
        sum_things = 0
        temp_var = set()
        for el in var:
            if sum_things + my_things[el] > weight:     # если сумма с добавление вещи превысит лимит, то 
                continue
            sum_things += my_things[el]
            temp_var.add(el)
        if temp_var not in variants:          # полученное до этого множество добавляем в список вариантов (если его там еще нет)
            variants.append(temp_var)

# проверим являются ли варианты подмножествами других вариантов, если да, то удалим эти варианты
i = 0
while i < len(variants):
    for j in range(0, len(variants)):
        if i == j:
            continue
        if variants[i] < variants[j]:
            variants.pop(i)
            break
    else:
        i += 1
    
print(f"Количество полученных вариантов: {len(variants)}")   
print() 
      
for var in sorted(variants, key=lambda x: sum(my_things[s] for s in x), reverse=True):
    print(*sorted(list(var)))
    wght = sum(my_things[s] for s in var)
    print(f"их общий вес {wght}")
    print() 

