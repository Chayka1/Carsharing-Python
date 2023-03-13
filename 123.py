from Carsharing.Cars import Cars


cars = [
    {'brand': 'BMW', 'model': 'M8', 'price': '100'},
    {'brand': 'Mers', 'model': 'G', 'price': '90'}
]

brand1 = input('Марка: ')
model1 = input('Модель: ')
price_per_hour1 = int(input('Цена за час в $: '))

car = Cars(brand1, model1, price_per_hour1)
cars.append({'brand': brand1, 'model': model1, 'price': price_per_hour1})








brand = input('Марка: ')
model = input('Модель: ')

for car in cars:
    if car['brand'] == brand and car['model'] == model:
        print('Архип пошел нахуй!')
        break
    else:
        print('Архип красавчик')


