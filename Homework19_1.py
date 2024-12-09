from wonderwords import RandomWord #pip install wonderwords
from colorama import Fore # pip install colorama

def with_index(iterable, start=0):
    count = start
    for elem in iterable:
        yield count, elem
        count += 1
r = RandomWord()

l = [r.word(), r.word(), r.word()]
for idx, item in with_index(l):
    print (f"{Fore.YELLOW} Слово:{Fore.BLACK} %s, {Fore.MAGENTA}"
           f"Позиция: {Fore.BLACK}%s" % (item, idx))
