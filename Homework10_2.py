from code_dump import end_file
try:
    a = float(input('Введи первое число: '))
    b = float(input('Введи второе число: '))
    result = (a ** 2) / b
except ZeroDivisionError:
    print ('Ошибка, число не может быть равно 0 ')
except ValueError:
    print ('Значение должно быть числом ')
finally:
    print (result)
end_file()