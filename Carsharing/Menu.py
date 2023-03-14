from Carsharing.Logic import Logic

add_car = 1
take_a_car_to_car_sharing = 2
list_of_available_cars = 3
quit = 4

log = Logic()


def get_menu_choice():
    while True:
        try:
            choice = int(input('Какую бы операцию вы хотели бы совершить:\n'
                               '1. Добавить машину\n'
                               '2. Взять машину в каршеринг\n'
                               '3. Список доступных машин\n'
                               '4. Выход\n'))
            if choice in [add_car, take_a_car_to_car_sharing, list_of_available_cars, quit]:
                return choice
            else:
                print('Введите число от 1 до 4')
        except ValueError:
            print('Введите число от 1 до 4')


def main():
    choice = 0
    while choice != quit:

        choice = get_menu_choice()

        if choice == add_car:
            log.add_car()
            input('Для продолжения нажмите Enter')

        elif choice == take_a_car_to_car_sharing:
            log.take_a_car_to_car_sharing()
            input('Для продолжения нажмите Enter')

        elif choice == list_of_available_cars:
            log.list_of_available_cars()
            input('Для продолжения нажмите Enter')

        elif choice == quit:
            break
