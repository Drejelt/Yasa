sentence = input("Введи свои данные: ")

dictionaries = sentence.split()
my_dict = {}

for dictionary in dictionaries:
    my_dict[dictionary] = my_dict.get(dictionary, 0) + 1

print(my_dict)

input ("Нажми Enter дабы завершить выполнение програмы: ")
