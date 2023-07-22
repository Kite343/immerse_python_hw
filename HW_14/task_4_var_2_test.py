# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

# * декоратор

import pytest

from task_1 import clean_text

@pytest.mark.parametrize("test_string, res_string",\
                         [
                             ("text str", 'text str'),
                             ("PytHoN", 'python'),
                             ("(text: str) -> str", 'text str  str'),
                             ("python не питон", 'python  '),
                             ("pYthOn, не питон!!!", 'python  ')
                         ])
def test_clean_text(test_string, res_string):
    assert clean_text(test_string) == res_string


if __name__ == '__main__':
    pytest.main(['-v'])


