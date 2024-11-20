from colorama import Fore # pip install colorama


def in_range(start, end, step=1):

    if step == 0:
        print (Fore.RED + f"Нехороший! {Fore.LIGHTMAGENTA_EX} Нельзя устанавливать шаг в 0.")
        raise ValueError(Fore.RED + f"Нехороший! {Fore.LIGHTMAGENTA_EX} Нельзя устанавливать шаг в 0.")
    if (step > 0 and start >= end) or (step < 0 and start <= end):
        return

    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step


print(list(in_range(1, 10, 2)))
