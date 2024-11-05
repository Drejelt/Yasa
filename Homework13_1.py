def count_local_variables():
    a = 10
    b = 20
    c = a + b
    d = 30


print("Количество локальных переменных:", count_local_variables.__code__.co_nlocals)