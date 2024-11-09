def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f"Ошибка: Аргумент не имеет типа {type_.__name__}")
                return False
            if len(arg) > max_length:
                print(f"Ошибка: длина аргумента превышает максимальную {max_length}")
                return False
            for symbol in contains:
                if symbol not in arg:
                    print(f"Ошибка: Аргумент не содержит требуемого символа '{symbol}'")
                    return False
            return func(arg)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} пьёт пепси в своём новеньком BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 пьёт пепси в своём новеньком BMW!'
