import json

def save_phonebook(phonebook, filename="phonebook.json"):
    #Сохраняет телефонную книгу в JSON-файл.
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(phonebook, file, indent=4)
    print("Телефонная книга сохранена в файл.")

def load_phonebook(filename="phonebook.json"):
    #Загружает телефонную книгу из JSON-файла, если файл существует.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            phonebook = json.load(file)
        print("Телефонная книга загружена из файла.")
        return phonebook
    except FileNotFoundError:
        print("Файл с телефонной книгой не найден, создаём новую телефонную книгу.")
        return {}
