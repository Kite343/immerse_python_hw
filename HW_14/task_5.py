# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rec_1 = Rectangle(5)
        self.rec_2 = Rectangle(6)
        self.rec_3 = self.rec_1 + self.rec_2
        self.rec_4 = self.rec_1 - self.rec_2

    # проверка типа при создании экземпляра класса
    def test_create(self):
        self.assertIsInstance(self.rec_1, Rectangle)
        self.assertEqual(Rectangle(5), self.rec_1)

    # проверка периметра
    def test_perimeter(self):
        self.assertEqual(self.rec_1.perimetr(), 20)

    # проверка площади
    def test_area(self):
        self.assertEqual(self.rec_1.square(), 25)

    # проверка не равенства прямоугольников
    def test_not_equal(self):
        self.assertFalse(self.rec_1 == self.rec_2)

    # проверка корректности передачи аргумента при создании экземпляра
    def test_type_argument(self):
        with self.assertRaises(TypeError):
            Rectangle('5') + Rectangle('6')

    def test_add(self):
        self.assertTrue(self.rec_1 + self.rec_2 == self.rec_3 )

    def test_add_2(self):
        self.assertEqual(self.rec_1 + self.rec_2, self.rec_3)

    def test_sub(self):
        self.assertTrue(self.rec_1 - self.rec_2 == self.rec_4 )


if __name__ == '__main__':
    unittest.main(verbosity=2)