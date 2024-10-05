import random

# Генерирую два случайных числа
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Создаю пример
expression = f"{num1} + {num2}"
correct_answer = num1 + num2

# Спрашиваю каков ответ
user_answer = input(f"Каков ответ {expression}? ")

# Проверяю правильность ответа
if user_answer.isdigit() and int(user_answer) == correct_answer:
    print("Правильно.")
else:
    print(f"Неправильно. Правильным ответ был: {correct_answer}.")

input ("Нажми Enter дабы завершить выполнение програмы: ")
