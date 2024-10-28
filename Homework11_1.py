def save_file(filename="myfile.txt"):
    #Сохраняет данные в наш txtшник.
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Hello file world!\n")


def read_from_file(filename="myfile.txt"):
    #Читает данные из нашего txtшника.
    with open(filename) as file:
        content = file.read()
    print(content)

#Вызываем функции
save_file()
read_from_file()