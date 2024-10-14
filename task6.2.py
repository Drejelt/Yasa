import random

list1 = []
list2 = []
list3 = []

# Если list1 длина меньше 10 символов то добавляем при помощи random случайные значения в диапозоне 1, 10
while len(list1) < 10:
    list1.append(random.randint(1, 10))

# Если list2 меньше длина 10 символов то добавляем при помощи random случайные значения в диапозоне 1, 10
while len(list2) < 10:
    list2.append(random.randint(1, 10))

# Ищу схожие елементы в list1 и list2, добавляю в list3
i = 0
while i < len(list1):
    if list1[i] in list2 and list1[i] not in list3:  # Проверяю на дубликаты
        list3.append(list1[i])
    i += 1

# Печатаю результат
print (list1, list2, list3)

input ("Нажми Enter дабы завершить выполнение програмы: ")
