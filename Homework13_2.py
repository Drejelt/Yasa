from random import randint

def outer_function():
    def inner_function(ran2):
        ran2 = randint (0, 99)
        return 'Привет из внутреней функции, твоё число: ' + str(ran2)

    return inner_function

stub_func = outer_function()

print(stub_func(None))
