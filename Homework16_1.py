from names_generator import generate_name # pip install names-generator
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, gender, grade, scholarship, student_id):
        super().__init__(name, age, gender)
        self.grade = grade
        self.scholarship = scholarship
        self.student_id = student_id

    def print_info(self):
        print(f'Моё имя {self.name}, возраст {self.age}, мой гендер {self.gender}, '
              f'у меня средний балл {self.grade}, я получаю стипендию в {self.scholarship} кредитов, '
              f'номер моего студенческого билета: {self.student_id}')


class Teacher(Person):
    def __init__(self, name, age, gender, salary, employee_id):
        super().__init__(name, age, gender)
        self.salary = salary
        self.employee_id = employee_id

    def print_info(self):
        print(f'Моё имя {self.name}, возраст {self.age} лет, мой гендер {self.gender}, '
              f'моя заработная плата {self.salary} кредитов, номер моего ID: {self.employee_id}')

NameTeacher = generate_name(style='capital')
Teacher23 = Teacher(NameTeacher, 35, "Мужской", 40, 9560123)
Teacher23.print_info()

NameStudent = generate_name(style='capital')
Student21 = Student(NameStudent, 18, "Мужской", 98, 15, 564124)
Student21.print_info()