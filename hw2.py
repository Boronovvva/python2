class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age 
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Ф.И.О - {self.fullname}, Возраст - {self.age}, Семейное положение - {self.is_married}")

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def count_salary(self):
        new_salary = self.salary + 3000 * self.experience
        print(f"Зарплата - {new_salary}")
    
    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт - {self.experience}")

teacher = Teacher("Нурлан уулу Барсбек", 21, "Разведённый", 5, 10000)
teacher.introduce_myself()
teacher.count_salary()
