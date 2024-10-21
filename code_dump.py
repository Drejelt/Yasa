def end_file():
    input("Нажми Enter дабы завершить выполнение програмы: ")
#№9
def favorite_movie():
    movie = input ('Введи название своего любимого фильма: ')
    return('Твой любимый фильм это ' + movie)

def i_dont_like_him():
    return (". Но он мне не нравиться.")

#№10
def oops():
    raise IndexError('Обнаружен IndexError.')
    #raise KeyError('Обнаружен KeyError')

def catching_error():
    try:
        oops()
    except IndexError:
        print('IndexError отловлен.')