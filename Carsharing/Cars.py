class Cars:
    def __init__(self, brand, model, price_per_hour):
        self.__model = model
        self.__brand = brand
        self.__price_per_hour = price_per_hour

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_price_per_hour(self, price_per_hour):
        self.__price_per_hour = price_per_hour

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price_per_hour(self):
        return self.__price_per_hour
