from Carsharing.Cars import Cars


class Logic:
    def __init__(self):
        self.cars = []

    def add_car(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        price_per_hour = int(input('Цена за час в $: '))
        car = Cars(brand, model, price_per_hour)
        self.cars.append({'brand': car.get_brand(), 'model': car.get_model(), 'price': car.get_price_per_hour()})

    def take_a_car_to_car_sharing(self):
        brand = input('Марка: ')
        model = input('Модель: ')
        for car in self.cars:
            if car['brand'] == brand and car['model'] == model:
                print(f"Стоимость данной машины в час составит {car['price']}$")
                i = self.cars.index({'brand': brand, 'model': model, 'price': car['price']})
                del self.cars[i]
                break
            else:
                print('Машину не найдено. Введите существующую модель!')

    def list_of_available_cars(self):
        for car in self.cars:
            print(f"{car['brand']}, {car['model']} : {car['price']}$/час")
