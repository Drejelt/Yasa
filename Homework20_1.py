import unittest
from unittest.mock import patch
import code_dump

class TestCodeDump(unittest.TestCase):
    @patch('builtins.input', return_value='Матрица')
    def test_favorite_movie(self, mock_input):
        result = code_dump.favorite_movie()
        self.assertEqual(result, 'Твой любимый фильм это Матрица')

    def test_i_dont_like_him(self):
        result = code_dump.i_dont_like_him()
        self.assertEqual(result, ". Но он мне не нравиться.")

    @patch('builtins.input', return_value='')
    def test_end_file(self, mock_input):
        try:
            code_dump.end_file()
        except Exception as e:
            self.fail(f'end_file() вызвала исключение: {e}')

if __name__ == '__main__':
    unittest.main()
