import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()

# Попробуйте запустить ваши тесты из урока 3.2 https://stepik.org/lesson/36285/step/13 с помощью PyTest. 
# В выводе найдите последнюю строку, скопируйте её и отправьте в это задание. Отправьте текст, который находится между  === и ===. 