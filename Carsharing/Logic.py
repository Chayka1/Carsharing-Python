from Carsharing.Cars import Cars


class Logic:
    def __init__(self):
        self.cars = {}
        self.cars_price = {}

    def add_car(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        price_per_hour = int(input('Цена за час в $: '))
        car = Cars(brand, model, price_per_hour)
        self.cars_price[car.get_model()] = car.get_price_per_hour()
        self.cars[car.get_brand()] = car.get_model()

    def take_a_car_to_car_sharing(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        for models in list(self.cars_price):
            if models == model:
                print(f'Стоимость данной машины в час составит {self.cars_price[model]}$')
                del self.cars_price[model]
            else:
                print('Машину не найдено. Введите существующую модель!')

    def list_of_available_cars(self):
        for car in self.cars:
            print(f'{car},{self.cars[car]}')

    def price_information(self):
        car_price = []
        car = []

        for carAndPrice in self.cars_price:
            i = f'{carAndPrice} {self.cars_price[carAndPrice]}$'
            car_price.append(i)

        for cars in self.cars:
            car.append(cars)

        for i in range(len(self.cars_price)):
            print(f'{car[i - 1]} {car_price[i - 1]}/час')