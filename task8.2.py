def make_country(name, capital):
    country_dict = {
        'name': name,
        'capital': capital
    }
    print(f"Страна: {country_dict['name']}, Столица: {country_dict['capital']}")
    
    return country_dict

make_country('Украина', 'Киев')

input ("Нажми Enter дабы завершить выполнение програмы: ")