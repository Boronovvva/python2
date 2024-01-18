class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
        
    @property
    def get_cpu(self):
        return self.__cpu
    
    @property
    def get_memory(self):
        return self.__memory
    
    def __make_computations(self):
        print(f"Сложение - {self.get_cpu + self.get_memory}, Вычитание - {self.get_cpu - self.get_memory},")
        print(f"Умножение - {self.get_cpu * self.get_memory}, Деление - {self.get_cpu / self.get_memory},")

    @property
    def get_make_computations(self):
        return self.__make_computations

computer = Computer(5, 512)
computer.get_make_computations()

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    @property
    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        print(f"Процессор - {self.get_cpu}, Память - {self.get_memory}, Карта памяти - {self.get_memory_card}")

laptop = Laptop("Core i5", "1t", 512)
laptop.info()