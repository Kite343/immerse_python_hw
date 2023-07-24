# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.

import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
        'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='task_1_log.log.', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        # logger.error("division by 0")
        logger.error(e)
    

if __name__ == "__main__":
    print(division(3, 2))
    print(division(3, 0))