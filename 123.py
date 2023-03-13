from Carsharing.Cars import Cars


cars = []

brand1 = input('Марка: ')
model1 = input('Модель: ')
price_per_hour1 = int(input('Цена за час в $: '))

car = Cars(brand1, model1, price_per_hour1)
cars.append({'brand': brand1, 'model': model1, 'price': price_per_hour1})

for car in cars:
    print(car['brand'])


