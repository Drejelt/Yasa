import unittest

from Homework21_1 import FileContextManager


class TestFFileContextManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("Hello World")

#Чтение/Запись
    def test_write_success(self):
        new_content = "New Hello World"
        with FileContextManager (self.test_file, "w") as f:
            f.write(new_content)

        with open(self.test_file, "r") as f:
            self.assertEqual(f.read(), new_content)

    def test_read_success(self):
        with FileContextManager (self.test_file, "r") as f:
            content = f.read()
            self.assertEqual(content, "Hello World")

    #Счётчик
    def test_counter_increment(self):
        initial_count = FileContextManager.counter
        with FileContextManager(self.test_file, "r"):
            pass
        self.assertEqual(FileContextManager.counter, initial_count + 1)

    def test_file_not_found(self):
        non_existent_file = "non_existent.txt"
        with self.assertRaises(FileNotFoundError):
            with FileContextManager (non_existent_file, "r"):
                pass



if __name__ == "__main__":
    unittest.main()