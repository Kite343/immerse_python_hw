# 📌 Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

# * doctest через unittest

import doctest
import unittest

import task_2

def load_tests(loader, tests, ignore):
        tests.addTests(doctest.DocTestSuite(task_2))
        return tests

if __name__ == '__main__':
    unittest.main(verbosity=2)