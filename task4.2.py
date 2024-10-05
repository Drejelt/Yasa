# Ввожу числа
phone_number = input("Введи номер телефона: ")

# Проверяю что чисел 10, что в phone_number только числа
if len(phone_number) == 10 and phone_number.isdigit():
    print("Правильно.")
else:
    print("Неправильно, попробуй ещё раз.")

input ("Нажми Enter дабы завершить выполнение програмы: ")
