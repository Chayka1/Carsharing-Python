from Carsharing.Cars import Car


class Logic:
    def __init__(self):
        self.cars = []

    def add_car(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        price_per_hour = int(input('Цена за час в $: '))
        car = Car(brand, model, price_per_hour)
        self.cars.append(car)

    def take_a_car_to_car_sharing(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        for car in self.cars:
            if car.brand == brand and car.model == model:
                print(f"Стоимость данной машины в час составит {car.price_per_hour}$")
                self.cars.remove(car)
                break
        else:
            print('Машину не найдено. Введите существующую модель!')

    def list_of_available_cars(self):
        for car in self.cars:
            print(f"{car.brand}, {car.model} : {car.price_per_hour}$/час")
