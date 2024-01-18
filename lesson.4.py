# Множественное наследование 

# class Car:
#     def __init__(self, model, year): 
#         self.model = model
#         self.year = year

#     def info(self):
#         print(f"Бренд - {self.model},  Год выпуска -  {self.year} ")

# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(self, model, year)
#         self.battery = battery

#     def drive(self):
#         print(f"машина - {self.model} едет на электричестве")

# class FuelCar(Car):
#     def __init__(self, model, year, fuel_bank):
#         Car.__init__(self, model, year)
#         self.fuel_bank = fuel_bank

#     def drive(self):
#         print(f"машина - {self.model} едет на топливе")

# class HybridCar(ElectricCar, FuelCar):
#     def __init__(self, model, year, battery, fuel_bank,speed):
#         ElectricCar.__init__(self, model, year, battery)
#         FuelCar.__init__(self, model, year, fuel_bank)
#         self.speed = speed 
#         # self.speed = speed 
#         # if self.speed < 60 :
#         #     print("Машина едет на электричестве")
#         # else:
#         #     print("Машина едет на топливе")
#         #     self.speed > 60

#     def drive(self):
#         if self.speed < 60 :
#             FuelCar.drive(self)
#         else:
#             ElectricCar.drive(self)
#             self.speed > 60

#         print(f"машина - {self.model} едет и на топливе и на электричестве")
        
# tesla = ElectricCar("Tesla - model x", 2024, 90)
# tesla.info()
# tesla.drive()

# matiz = FuelCar("Matiz - 3", 2020,30)
# matiz.info()
# matiz.drive()

# lexus = HybridCar("Lexus - 300es", 2020,40,60, 90)
# lexus.info()
# lexus.drive()


# Магические методы

class Car:
    def __init__(self, model, year): 
         self.model = model
         self.year = year

    # def info(self):
    #     print(f"Бренд - {self.model},  Год выпуска -  {self.year} ")

    def __str__(self): # __str__ == print
        return f"Бренд - {self.model},  Год выпуска -  {self.year} "


bwm = Car ("bwm - m5", 2022)
# bwm.info()
print(bwm)