phone_number = input("Введите номер телефона: ")

if len(phone_number) == 10 and phone_number.isdigit():
    print("Правильный номер телефона.")
else:
    print("Неправильно, попробуй ещё раз.")
