def make_operation(operator, *args):
    if operator == '+':
        number= 0
        for plus in args:
            number += plus
    elif operator == '-':
        number= args[0]
        for minus in args[1:]:
            number -= minus
    elif operator == '*':
        number= 1
        for multiplied in args:
            number *= multiplied
    return number

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
input ("Нажми Enter дабы завершить выполнение програмы: ")