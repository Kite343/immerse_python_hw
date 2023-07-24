# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime, timedelta, date
import logging

logging.basicConfig(filename='task_4.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def convert_to_date(text: str) -> date:
    months = {'января': 1, 'февраля': 2, "марта": 3, 
              "апреля": 4, "мая": 5, "июня": 6,
              "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
    days = {"понедельник": 0, "вторник": 1, "среда": 2, "четверг": 3, 
            "пятница": 4, "суббота": 5, "воскресенье": 6}
    text = text.split()
    if len(text) != 3:
        logger.critical('Неверный формат ввода!!!')
        raise ValueError
    num_day_of_week, day_of_week, month = text
    num_day_of_week = num_day_of_week[:-2]
    if not num_day_of_week.isdecimal():
        logger.critical('Неверный формат ввода (не цифра)!!!')
        raise ValueError
    num_day_of_week = int(num_day_of_week)
    # print(f'{num_day_of_week = }')

    if day_of_week not in days:
        logger.critical('Неверный формат ввода!!!')
        raise ValueError
    day_of_week = days[day_of_week]
    # print(f'{day_of_week = }')

    if month not in months:
        logger.critical('Неверный формат ввода!!!')
        raise ValueError
    month = months[month]
    # print(f'{month = }')

    original_date = date(year=datetime.now().year, month=month, day=1)
    # print(original_date)
    prev_day = 0
    num_week = 0
    delta = timedelta(days=1)


    while prev_day < original_date.day:
        if original_date.weekday() == day_of_week:
            num_week += 1
        if num_week == num_day_of_week:
            return original_date
        prev_day = original_date.day
        original_date += delta
    logger.critical('Неверный формат ввода!!!')
    raise ValueError


if __name__ == '__main__':
    text = '1-й четверг ноября'
    text = '3-я среда мая'
    text = '3-й четверг июля'
    text = '1-й воскресенье июля'
    text = 'четверг июля'
    print(convert_to_date(text))

