# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


import datetime

# константы
TAX_WEALTH = 0.1
MAX_SUM = 5_000_000
NOMINAL = 50
NUMBER_OPERATION = 3
BET = 0.03
PERCENT_POP = 0.015
MIN_PRICE_POP = 30
MAX_PRICE_POP = 600

log_user = []

# внесение
def add_money(sum, n):    
    sum = tax_wealth(sum)
    print(f"Ваш баланс {sum}")

    count = 0
    while True:
        count = input(f"Введите сумму кратную {NOMINAL} у.е.\n")
        if count.isdigit() and (int(count) % 50 == 0):
            count = int(count)
            break
    sum += count
    log_user.append((datetime.datetime.now(), "пополнение", count))
    if n % NUMBER_OPERATION == 0:
        print("Вам начислены проценты")
        bet = round(sum * BET, 2)
        log_user.append((datetime.datetime.now(), "начисление процентов", bet))
        sum += bet
    print(f"Ваш баланс {sum}")
    return sum

# снятие
def pop_money(sum, n):
    sum = tax_wealth(sum)

    print(f"Ваш баланс {sum}")

    count = 0
    while True:
        count = input(f"Введите нужную сумму\n")
        if count.isdigit():
            count = int(count) 
            break
    sum_percent_pop = round(count * PERCENT_POP, 2)
    
    if sum_percent_pop < MIN_PRICE_POP:
        sum_percent_pop = MIN_PRICE_POP
    elif sum_percent_pop > MAX_PRICE_POP:
        sum_percent_pop = MAX_PRICE_POP
    
    sum_pop = count + sum_percent_pop
    
    if sum_pop > sum:
        print("Недостаточно средств")
        log_user.append((datetime.datetime.now(), "снятие", 0))
    else:
        sum -= sum_pop
        log_user.append((datetime.datetime.now(), "снятие", count))
        log_user.append((datetime.datetime.now(), "проценты за снятие", sum_percent_pop))

    print(f"Ваш баланс {sum}")

    if n % NUMBER_OPERATION == 0:
        bet = round(sum * BET, 2)
        log_user.append((datetime.datetime.now(), "начисление процентов", bet))
        sum += bet
        print("Вам начислены проценты")
        print(f"Ваш баланс {sum}")
    return sum

# налог на богатство
def tax_wealth(sum):
    if sum > MAX_SUM:
        print(f"Ваш баланс {sum}")
        print("Был снят налог на богатство")
        tax_w = round(sum * TAX_WEALTH, 2)
        log_user.append((datetime.datetime.now(), "снятие налог на богатство", tax_w))
        sum -= tax_w
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
            print(f"Ваш баланс {sum_user}")
            start = False

for log in log_user:
    print(*log) 
