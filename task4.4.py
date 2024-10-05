# Наше имя в маленьком регистре
stored_name = "valentyn"

# Ask for user input
user_input = input("Пожалуйста введи своё имя: ")

# Проверяю, совпадает ли введенное имя с сохраненным.
is_equal = user_input.lower() == stored_name

# Печатаю резулультат
print(is_equal)
