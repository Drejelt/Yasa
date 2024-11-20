import re
from colorama import Fore

class EmailValidator:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError(f"{Fore.RED} Неверный адрес электроной почты: {email}")
        else:
            print (f"{Fore.GREEN} Верный адрес электроной почты: {email}")


EmailValidator.validate(input('Введите адрес электронной почты: '))
