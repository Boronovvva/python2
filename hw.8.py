# дз 

import sqlite3

connect = sqlite3.connect('cars.db')
cursor = connect.cursor()
        
cursor.execute("""CREATE TABLE IF NOT EXISTS cars_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_title TEXT (100) NOT NULL,
                price FLOAT DEFAULT 0.0,
                quantity INTEGER NOT NULL DEFAULT 0
                        );""")
        
        
class Car():

    def __init__(self):
        self.car_title = None
        self.price = 0.0
        self.quantity = 0
        

    def add_car(self, car_title, price, quantity):
        self.car_title = car_title
        self.price = price
        self.quantity = quantity
        cursor.execute('''INSERT INTO cars_list (car_title, price, quantity)
                       VALUES(?, ?, ?)''',(car_title, price, quantity))
        connect.commit()

    def delete_car(self,car_id):
        self.car_id = car_id
        cursor.execute('''DELETE FROM cars_list WHERE id = ?''', (car_id,))
        connect.commit()
    
# доп дз
    def select_cheaper_cars():

        cursor.execute('''SELECT * FROM cars_list WHERE price < 100.0''')
        cheaper_cars = cursor.fetchall()
        
        
        if cheaper_cars:
            print("Автомобили дешевле 100 долларов:")
            for car in cheaper_cars:
                print(f"ID: {car[0]}, Car Title: {car[1]}, Price: ${car[2]}, Quantity: {car[3]}")
        else:
            print("Машин дешевле 100 долларов не найдено.")
        
        connect.commit()
    
car = Car()
car.add_car("Toyota Camry", 25000.0, 5)
car.delete_car(1)
car.select_cheaper_cars()
