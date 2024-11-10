class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f"Здравствуйте, меня зовут {self.firstname} {self.lastname} мне {self.age} лет."

placeholder = Person("Карл", "Джонсон", 26)
print (placeholder.talk())

