# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей

camping_friends = {
    "Вася": ("топор", "палатка", "кружка", "хлеб", "соль", "ложка", "лопата"),
    "Петя": ("пила", "кружка", "ложка", "соль", "картошка", "бинт"),
    "Дима": ("кружка", "ложка", "котелок", "тарелка", "бинт", "лопата"),
}
names = [*camping_friends.keys()]

# Какие вещи взяли все три друга
everyone_has = set(camping_friends[names[0]])
for name in names[1:]:
    everyone_has = everyone_has & set(camping_friends[name])
print("Все друзья взяли")
print(*everyone_has)
print()

# Какие вещи уникальны, есть только у одного друга
for name in names:
    exclusive = set(camping_friends[name])
    for name_compare in names:
        if name == name_compare:
            continue
        exclusive = exclusive - set(camping_friends[name_compare])
    print(f"Только у {name} есть")
    print(*exclusive)
    print()


# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует

for name in names:
    chek_names = names.copy()
    chek_names.remove(name)
    everyone_has = set(camping_friends[chek_names[0]])
    for n in chek_names[1:]:
        everyone_has = everyone_has & set(camping_friends[n])
    everyone_has = everyone_has - set(camping_friends[name])
    print(f"У всех, кроме {name} есть")
    print(*everyone_has)
    print()


