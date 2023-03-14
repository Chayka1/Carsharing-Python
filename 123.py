from Carsharing.Cars import Car


cars = []

brand = input('Марка: ')
model = input('Модель: ')
price_per_hour1 = int(input('Цена за час в $: '))

car = Car(brand, model, price_per_hour1)
cars.append(car)


