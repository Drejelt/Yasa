# Ввожу значение при помощи input
input_str = input("Введите слово: ")

# Проверяю меньше ли длина строки 2х
if len(input_str) < 2:
    result = ""
else:
    # Получаю два первых и два последних символа
    result = input_str[:2] + input_str[-2:]

# Печатаю результат
print("Результат:", result)
