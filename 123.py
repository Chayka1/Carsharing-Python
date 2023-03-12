class Cars:
    def __init__(self, brand, model, price_per_hour, commission):
        self.commission = commission
        self.price_per_hour = price_per_hour
        self.model = model
        self.brand = brand


cars = {}


def add_car():
    i = len(cars)
    car = Cars('BMW', 'M8', 100, 10)
    cars[car.model()] = car.brand()


def take_a_car_to_car_sharing(self, brand, model):
    if model == self.cars:
        print(f'Стоимость данной машины в час составит ')
