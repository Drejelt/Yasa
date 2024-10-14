numbers = list(range(1, 101))
numbers2 = []

i = 0

while i < len(numbers):
    if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
        numbers2.append(numbers[i])
    i += 1

print (numbers2)

input ("Нажми Enter дабы завершить выполнение програмы: ")
