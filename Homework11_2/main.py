from storage import load_phonebook
from contacts import add_contact, search_by_first_name, search_by_last_name, search_by_full_name, search_by_phone, search_by_city, remove_contact, update_contact

# Загрузка телефонной книги из файла при запуске программы
phonebook = load_phonebook()

while True:
    action = input(
        "Введи действие (add/search_name/search_surname/search_full_name/search_phone/search_city/remove/update/exit): ").strip().lower()

    if action == 'add':
        first_name = input("Введи имя: ").strip()
        last_name = input("Введи фамилию: ").strip()
        phone = input("Введи номер телефона: ").strip()
        city = input("Введи город: ").strip()
        add_contact(phonebook, first_name, last_name, phone, city)

    elif action == 'search_name':
        first_name = input("Введи имя для поиска: ").strip()
        search_by_first_name(phonebook, first_name)

    elif action == 'search_surname':
        last_name = input("Введи фамилию для поиска: ").strip()
        search_by_last_name(phonebook, last_name)

    elif action == 'search_full_name':
        first_name = input("Введи имя: ").strip()
        last_name = input("Введи фамилию: ").strip()
        search_by_full_name(phonebook, first_name, last_name)

    elif action == 'search_phone':
        phone = input("Введи номер телефона для поиска: ").strip()
        search_by_phone(phonebook, phone)

    elif action == 'search_city':
        city = input("Введи город для поиска: ").strip()
        search_by_city(phonebook, city)

    elif action == 'remove':
        phone = input("Введи номер телефона для удаления: ").strip()
        remove_contact(phonebook, phone)

    elif action == 'update':
        phone = input("Введи номер телефона для обновления: ").strip()
        if phone in phonebook:
            new_first_name = input("Введи новое имя (оставь пустым, если не нужно менять): ").strip()
            new_last_name = input("Введи новую фамилию (оставь пустым, если не нужно менять): ").strip()
            new_city = input("Введи новый город (оставь пустым, если не нужно менять): ").strip()
            update_contact(phonebook, phone, new_first_name or None, new_last_name or None, new_city or None)
        else:
            print(f'Контакт с номером "{phone}" не найден.')

    elif action == 'exit':
        print("Выход из программы.")
        break

    else:
        print("Неверное действие.")
