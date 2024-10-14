import random

random_number = random.randint(1, 10)

user_input = int(input('Введи число от 1 до 10: '))

if user_input == random_number:
    print ('Поздравляю, везучий ты человек')
else:
        print ('Неправильно, попробуй ещё раз.')
        
input ("Нажми Enter дабы завершить выполнение програмы: ")