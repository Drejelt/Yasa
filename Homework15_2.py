class Dog:
    age_factor = 7
    def __init__(self, normal_age):
        self.normal_age = normal_age

    def human_age(self):
        return self.age_factor * self.normal_age

woof_age = 5
dog = Dog(woof_age)
print('Возраст собаки в человеческом эквиваленте: ' + str(dog.human_age()))
