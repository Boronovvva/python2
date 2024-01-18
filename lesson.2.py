#Основные принципы ООП 

class Animals:
    def __init__(self, breed, classes, color, age):
        self.breed = breed
        self.classes = classes
        self.color = color
        self.age = age

    def info(self):
        print(f"{self.breed},{self.classes}, {self.color}, {self.age}")

class Dog(Animals):
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        
    def info(self):
        print(f"{self.breed},{self.classes}, {self.color}, {self.age},  кол-во лап-{self.paws}")
        self.paws= 4

    def make_sound(self):
        print("Gaf-Gaf")

class Cat(Animals):
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        
    def info(self):
        print(f"{self.breed},{self.classes}, {self.color}, {self.age}")

    def make_sound(self):
        print("Meow")


class Cow(Animals):
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        
    def info(self):
        print(f"{self.breed},{self.classes}, {self.color}, {self.age},  кол-во рог-{self.hourse}")

    def make_sound(self):
        print("Moo")


dog = Dog("Haski","млекопитающий","grey", 3)
dog.make_sound()
        
cat = Cat("Ryjik","млекопитающий","orange", 1)
cat.make_sound()

cow = Cow("Murka","млекопитающий","black", 3)
cow.make_sound()
        