cars = [
    {'brand': 'BMW', 'model': 'M8', 'price': '100'},
    {'brand': 'Mers', 'model': 'G', 'price': '90'}
]

brand = input('Марка: ')
model = input('Модель: ')

for car in cars:
    if car['brand'] == brand and car['model'] == model:
        print('Архип пошел нахуй!')
        break
    else:
        print('Архип красавчик')
