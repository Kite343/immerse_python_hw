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

variants = []
things_name = [*my_things.keys()]
n = len(things_name) - 1
# берем 1 вещь и к ней прибавляем другие, пока не достигнем максимума не привышающего нужный вес
# каждый цикл первая положенная вещь меняется
# каждую итерацию (второй цикл) меняем порядок добавления вещей (делаем сдвиг), чтобы перебрать разные варианты
for thing in things_name:
    if my_things[thing] > weight:
        continue
    temp_var = {thing,}
    temp = things_name.copy()
    temp.remove(thing)
    sum_things = my_things[thing] 
    for _ in range(n):
        temp.append(temp.pop(0))                      # меняем порядок остальной части списка
        for el in temp:
            if sum_things + my_things[el] > weight:     # если сумма с добавление вещи превысит лимит, то 
                continue
            sum_things += my_things[el]
            temp_var.add(el)
        if temp_var not in variants:          # полученное до этого множество добавляем в список вариантов (если его там еще нет)
            variants.append(temp_var)
        temp_var = {thing,}
        sum_things = my_things[thing] 
    
print(f"Количество полученных вариантов: {len(variants)}")   
print() 
      
for var in sorted(variants, key=lambda x: sum(my_things[s] for s in x), reverse=True):
    print(*sorted(list(var)))
    wght = sum(my_things[s] for s in var)
    print(f"их общий вес {wght}")
    print() 

