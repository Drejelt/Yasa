import unittest
from unittest.mock import patch
from phonebook.contacts import add_contact, search_by_first_name

class TestContacts(unittest.TestCase):
    @patch('phonebook.contacts.save_phonebook')
    def test_add_contact(self, mock_save):
        phonebook = {}
        add_contact(phonebook, "John", "Doe", "12345", "New York")
        self.assertIn("12345", phonebook)
        self.assertEqual(phonebook["12345"], {
            'first_name': 'John',
            'last_name': 'Doe',
            'city': 'New York'
        })
        mock_save.assert_called_once_with(phonebook)

    def test_search_by_first_name(self):
        phonebook = {
            "12345": {'first_name': 'John', 'last_name': 'Doe', 'city': 'New York'},
            "67890": {'first_name': 'Jane', 'last_name': 'Smith', 'city': 'Los Angeles'}
        }
        with patch('builtins.print') as mock_print:
            search_by_first_name(phonebook, "John")
        mock_print.assert_called_with("Номер: 12345, Имя: John, Фамилия: Doe, Город: New York")
