class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print('woof woof')

class Cat(Animal):
    def talk(self):
        print('meow')

def cast_vote(animal: Animal):
    animal.talk()

cast_vote(Cat())
cast_vote(Dog())
