from phonebook.storage import save_phonebook

def add_contact(phonebook, first_name, last_name, phone, city):
    #Добавляет новый контакт в телефонную книгу.
    if phone in phonebook:
        print(f'Номер "{phone}" уже существует в телефонной книге.')
    else:
        phonebook[phone] = {'first_name': first_name, 'last_name': last_name, 'city': city}
        print(f'Контакт "{first_name} {last_name}" добавлен в телефонную книгу.')
        save_phonebook(phonebook)

def search_by_first_name(phonebook, first_name):
    #Ищет контакты по имени.
    results = {phone: info for phone, info in phonebook.items() if info['first_name'].lower() == first_name.lower()}
    if results:
        for phone, info in results.items():
            print(f"Номер: {phone}, Имя: {info['first_name']}, Фамилия: {info['last_name']}, Город: {info['city']}")
    else:
        print(f'Контакты с именем "{first_name}" не найдены.')

def search_by_last_name(phonebook, last_name):
    #Ищет контакты по фамилии.
    results = {phone: info for phone, info in phonebook.items() if info['last_name'].lower() == last_name.lower()}
    if results:
        for phone, info in results.items():
            print(f"Номер: {phone}, Имя: {info['first_name']}, Фамилия: {info['last_name']}, Город: {info['city']}")
    else:
        print(f'Контакты с фамилией "{last_name}" не найдены.')

def search_by_full_name(phonebook, first_name, last_name):
    #Ищет контакт по полному имени.
    results = {phone: info for phone, info in phonebook.items() if info['first_name'].lower() == first_name.lower() and info['last_name'].lower() == last_name.lower()}
    if results:
        for phone, info in results.items():
            print(f"Номер: {phone}, Имя: {info['first_name']}, Фамилия: {info['last_name']}, Город: {info['city']}")
    else:
        print(f'Контакты с именем "{first_name} {last_name}" не найдены.')

def search_by_phone(phonebook, phone):
    #Ищет контакт по номеру телефона.
    if phone in phonebook:
        info = phonebook[phone]
        print(f"Номер: {phone}, Имя: {info['first_name']}, Фамилия: {info['last_name']}, Город: {info['city']}")
    else:
        print(f'Контакт с номером "{phone}" не найден.')

def search_by_city(phonebook, city):
    #Ищет контакты по городу.
    results = {phone: info for phone, info in phonebook.items() if info['city'].lower() == city.lower()}
    if results:
        for phone, info in results.items():
            print(f"Номер: {phone}, Имя: {info['first_name']}, Фамилия: {info['last_name']}, Город: {info['city']}")
    else:
        print(f'Контакты в городе "{city}" не найдены.')

def remove_contact(phonebook, phone):
    #Удаляет контакт по номеру телефона.
    if phone in phonebook:
        del phonebook[phone]
        print(f'Контакт с номером "{phone}" удалён.')
        save_phonebook(phonebook)
    else:
        print(f'Контакт с номером "{phone}" не найден.')

def update_contact(phonebook, phone, new_first_name=None, new_last_name=None, new_city=None):
    #Обновляет контакт по номеру телефона.
    if phone in phonebook:
        if new_first_name:
            phonebook[phone]['first_name'] = new_first_name
        if new_last_name:
            phonebook[phone]['last_name'] = new_last_name
        if new_city:
            phonebook[phone]['city'] = new_city
        print(f'Контакт с номером "{phone}" обновлён.')
        save_phonebook(phonebook)
    else:
        print(f'Контакт с номером "{phone}" не найден.')
