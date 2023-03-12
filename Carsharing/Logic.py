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
        self.cars[car.get_model()] = car.get_brand()

    def take_a_car_to_car_sharing(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        key_copy_cars_price = tuple(self.cars_price.keys())
        for models in key_copy_cars_price:
            if models == model:
                print(f'Стоимость данной машины в час составит {self.cars_price[model]}$')
                del self.cars_price[model]
                del self.cars[model]
                break
            else:
                print('Машину не найдено. Введите существующую модель!')

    def list_of_available_cars(self):
        for car in self.cars:
            print(f'{self.cars[car]},{car}')

    def price_information(self):
        car_price = []
        car = []

        for carAndPrice in self.cars_price:
            car_price.append(f'{carAndPrice} {self.cars_price[carAndPrice]}$')

        for cars in self.cars:
            car.append(self.cars[cars])

        for i in range(len(self.cars_price)):
            print(f'{car[i - 1]} {car_price[i - 1]}/час')
