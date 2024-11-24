import unittest
from unittest.mock import mock_open, patch
from phonebook.storage import save_phonebook

class TestStorage(unittest.TestCase):
    def test_save_phonebook(self):
        phonebook = {'12345': {'first_name': 'John', 'last_name': 'Doe', 'city': 'New York'}}
        mocked_open = mock_open()

        with patch('builtins.open', mocked_open):
            save_phonebook(phonebook, filename="test_phonebook.json")

        written_data = "".join(call.args[0] for call in mocked_open().write.mock_calls)

        expected_data = (
            '{\n'
            '    "12345": {\n'
            '        "first_name": "John",\n'
            '        "last_name": "Doe",\n'
            '        "city": "New York"\n'
            '    }\n'
            '}'
        )

        self.assertEqual(written_data, expected_data)
