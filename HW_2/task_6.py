# def 

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# константы
TAX_WEALTH = 0.1
MAX_SUM = 5_000_000
NOMINAL = 50
NUMBER_OPERATION = 3
BET = 0.03
PERCENT_POP = 0.015
MIN_PRICE_POP = 30
MAX_PRICE_POP = 600

# внесение
def add_money(sum, n):    
    sum = tax_wealth(sum)

    count = count_money()
    sum += count * NOMINAL
    if n % NUMBER_OPERATION == 0:
        sum *= (1 + BET)
    return sum

# снятие
def pop_money(sum, n):
    sum = tax_wealth(sum)

    count = count_money()
    sum_percent_pop = count * NOMINAL * PERCENT_POP
    
    if sum_percent_pop < MIN_PRICE_POP:
        sum_percent_pop = MIN_PRICE_POP
    elif sum_percent_pop > MAX_PRICE_POP:
        sum_percent_pop = MAX_PRICE_POP
    
    sum_pop = count * NOMINAL + sum_percent_pop
    
    if sum_pop > sum:
        print("Недостаточно средств")
    else:
        sum -= sum_pop

    if n % NUMBER_OPERATION == 0:
        sum *= (1 + BET)
    return sum

# налог на богатство
def tax_wealth(sum):
    if sum > MAX_SUM:
        print("Был снят налог на богатство")
        sum *= (1 - TAX_WEALTH)
    return sum

# выбор действия
def choose_action():
    while True:
        com = "Выберите действие\n \
            1 - пополнить\n \
            2 - снять\n \
            3 - выйти\n"
        choice = input(com)
        if choice.isdigit() and choice in ("1", "2", "3"):
            return choice
        else:
            print("Введите номер нужной операции (это должно быть число)")

# количество денег для внесения или снятия
def count_money():
    while True:
        count = input(f"Введите необходтмое количество купюр по {NOMINAL} у.е.\n")
        if count.isdigit(): return int(count)


# программа
sum_user = 0
start = True
operation_count = 0
while start:
    choice = choose_action()
    match choice:
        case '1':
            operation_count += 1
            sum_user = add_money(sum_user, operation_count)
        case '2':
            operation_count += 1
            sum_user = pop_money(sum_user, operation_count)
        case '3':
            sum_user = tax_wealth(sum_user)
            start = False
    print(sum_user)

