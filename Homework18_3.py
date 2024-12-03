from functools import wraps
from colorama import Fore # pip install colorama

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except ValueError:
                print(Fore.RED + f"Ошибка: невозможно преобразовать '{result}' в int.")
                raise ValueError(f"Невозможно преобразовать '{result}' в int.")
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, (str, int, float, bool)):
                print(Fore.RED + f"Ошибка: невозможно преобразовать '{result}' в str.")
                raise ValueError(f"Невозможно преобразовать '{result}' в str.")
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                if result.lower() in ('true', '1'):
                    return True
                elif result.lower() in ('false', '0'):
                    return False
            elif isinstance(result, (int, float)):
                return bool(result)
            print(Fore.RED + f"Ошибка: невозможно преобразовать '{result}' в bool.")
            raise ValueError(f"Невозможно преобразовать '{result}' в bool.")
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except ValueError:
                print(Fore.RED + f"Ошибка: невозможно преобразовать '{result}' в float.")
                raise ValueError(f"Невозможно преобразовать '{result}' в float.")
        return wrapper

@TypeDecorators.to_int
def return_as_is_int(string: str):
    return string

@TypeDecorators.to_float
def return_as_is_float(string: str):
    return string

@TypeDecorators.to_bool
def return_as_is_bool(string: str):
    return string

@TypeDecorators.to_str
def return_as_is_str(value):
    return value

#try:
    assert return_as_is_int('25') == 25
    assert return_as_is_float('25.5') == 25.5
    assert return_as_is_bool('True') is True
    assert return_as_is_str(25) == '25'

    # Вызываю ошибки
#     return_as_is_int('abc')
# except ValueError as e:
#     print(Fore.YELLOW + f"Поймано исключение: {e}")
#
# try:
#     return_as_is_float('abc')
# except ValueError as e:
#     print(Fore.YELLOW + f"Поймано исключение: {e}")
#
# try:
#     return_as_is_bool('not_a_bool')
# except ValueError as e:
#     print(Fore.YELLOW + f"Поймано исключение: {e}")
#
# try:
#     return_as_is_str({'key': 'value'})
# except ValueError as e:
#     print(Fore.YELLOW + f"Поймано исключение: {e}")
