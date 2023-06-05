# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def multiplication_table():
    print('Таблица умножения')
 
    for i in range(2, 10):
        for k in range(2, 10):
            print(f'{k} * {i} = {k * i}\t', end='')
        print('')

multiplication_table()