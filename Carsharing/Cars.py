class Car:
    def __init__(self, brand, model, price_per_hour):
        self.brand = brand
        self.model = model
        self.price_per_hour = price_per_hour

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def price_per_hour(self):
        return self.__price_per_hour

    @price_per_hour.setter
    def price_per_hour(self, value):
        self.__price_per_hour = value
