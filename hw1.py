# # ДЗ 1 
# class Fruits:
#     def __init__(self,name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#     def info(self):
#         print(f"Название - {self.name}, \nЦвет - {self.color}, \nМасса - {self.weight} кг\n") 

# melon = Fruits("Melon", "yelllow", 1)
# avocado = Fruits("Avocado", "green", 2)
# grape = Fruits("Grape", "black",3)

# melon.info()
# avocado.info()
# grape.info()

# # ДЗ 2  Доп дз 
# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.fuel = 0
      
        
#     def refuel(self,re):
#         self.re = re
#         if self.re > 40:
#             print("Можно заправить на 40 литров")
    
#         else:
#             print("Вы заправились")
#             self.fuel=+ 40

#     def drive(self,city,distence):
#         self.city = city
#         self.distence = distence
#         if self.distence == 400 and self.fuel == 40:

#             print(f"Машина -{self.model} {self.year} года, {self.color} цвета едет в {self.city} c дистанцией {self.distence} км ")
        
#         elif self.distence != 400:
#             print("На одной заправке можно проехать только 400 км") 

# maybach= Car("Maybach", 2020,"Black")
# maybach.refuel(40)
# maybach.drive("Osh", 400)
