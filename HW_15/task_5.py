# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

from task_4 import convert_to_date

import argparse
from datetime import datetime

months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 
          6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября',
          10: 'октября', 11: 'ноября', 12: 'декабря'}

days = {0: 'понедельник', 1: 'вторник', 2: 'среда', 
        3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

def parser():
    parser = argparse.ArgumentParser(description='Our parser')
    parser.add_argument('-n', metavar='number', default='1-й', help='enter day')
    parser.add_argument('-w', metavar='week_day', default=days[datetime.now().weekday()], help='enter week_day')
    parser.add_argument('-m', metavar='month', default=months[datetime.now().month], help='enter month')
    args = parser.parse_args()
    print(args)
    print(convert_to_date(f'{args.n} {args.w} {args.m}'))

if __name__ == '__main__':
    parser()

"""
python HW_15\\task_5.py -n 3-й -w четверг -m июля
python HW_15\\task_5.py -n 3-й -w понедельник -m июля
python HW_15\\task_5.py
"""