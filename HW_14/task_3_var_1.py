# 📌 Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from task_1 import clean_text

class TestCaseName(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(clean_text("text str"), 'text str', msg="Строка была изменена")

    def test_registr(self):
        self.assertEqual(clean_text("PytHoN"), 'python')

    def test_signs(self):
        self.assertEqual(clean_text("(text: str) -> str"), 'text str  str')

    def test_other_letters(self):
        self.assertEqual(clean_text("python не питон"), 'python  ')

    def test_all(self):
        self.assertEqual(clean_text("pYthOn, не питон!!!"), 'python  ')
    

if __name__ == '__main__':
    unittest.main(verbosity=2)