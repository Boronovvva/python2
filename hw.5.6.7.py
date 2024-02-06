# кондитерский магазин 

class PastryChef:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0

    def bake(self, pastry_name):
        exp_gained = len(pastry_name) * 10
        self.exp += exp_gained
        print(f"{self.name} запеченный {pastry_name}! (+{exp_gained} exp)")
        self.level_up()

    def level_up(self):
        if self.exp >= self.level * 100:
            self.exp -= self.level * 100
            self.level += 1
            print(f"{self.name} выровнен до уровня {self.level}!")

def main():
    chef_name = input("Введите имя вашего кондитера: ")
    chef = PastryChef(chef_name)

    print(f"Добро пожаловать, {chef.name}!")
    print("Приступим к выпечке!")
    while True:
        pastry_name = input("Введите название теста, которое нужно испечь (или Выйдите, чтобы выйти).): ")
        if pastry_name.lower() == 'quit':
            print(f"Спасибо за игру, {chef.name}!")
            break
        chef.bake(pastry_name)

if __name__ == "__main__":
    main()



