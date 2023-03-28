from Carsharing.Cars import Car
import sqlite3


class Logic:

    def __init__(self):
        self.conn = sqlite3.connect('carsharing.db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS cars (brand TEXT, model TEXT, price_per_hour INTEGER)')

    def add_car(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        price_per_hour = int(input('Цена за час в $: '))
        car = Car(brand, model, price_per_hour)
        self.cur.execute('INSERT INTO cars VALUES (?, ?, ?)', (brand.upper(), model.upper(), price_per_hour))
        self.conn.commit()

    def take_a_car_to_car_sharing(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        self.cur.execute('SELECT * FROM cars WHERE brand = ? AND model = ?', (brand.upper(), model.upper()))
        row = self.cur.fetchone()
        if row is not None:
            car = Car(*row)
            print(f"Стоимость данной машины в час составит {car.price_per_hour}$")
            self.cur.execute('DELETE FROM cars WHERE brand = ? AND model = ?', (brand.upper(), model.upper()))
            self.conn.commit()
        else:
            print('Машину не найдено. Введите существующую модель!')

    def list_of_available_cars(self):
        self.cur.execute('SELECT * FROM cars')
        rows = self.cur.fetchall()
        if len(rows) == 0:
            print('Список доступных машин пуст')
        else:
            for row in rows:
                print(f"{row[0]}, {row[1]} : {row[2]}$/час")
