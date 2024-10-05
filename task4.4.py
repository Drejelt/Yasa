# Наше имя с маленьким регистром
stored_name = "valentyn"

# Просим ввести имя
user_input = input("Пожалуйста, введи своё имя: ")

# Проверяем правильно ли введино имя
is_equal = user_input.lower() == stored_name

# Печатаю результат
print(is_equal)

input ("Нажми Enter дабы завершить выполнение програмы: ")