name = "Valentyn"
day = "Monday"

# Использую способ формотирования при помощи f-string
message_1 = f"Good day {name}! {day} is a perfect day to learn some python."

# Использую способ при помощи .format()
message_2 = "Good day {}! {} is a perfect day to learn some python.".format(name, day)


# Печатаю результаты
print(message_1)
print(message_2)