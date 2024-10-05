import random

# Генерирую два случайных числа и случайный оператор
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Составляю пример
expression = f"{num1} + {num2}"
correct_answer = num1 + num2

# Спрашиваем ответ через input.
user_answer = input(f"Каков ответ {expression}? \n")

# Проверяем правильно ли ответил пользователь
if user_answer.isdigit() and int(user_answer) == correct_answer:
    print("Правильно.")
else:
    print(f"Неправильно, попробуй еще раз. Правильный ответ равняеться {correct_answer}.")
