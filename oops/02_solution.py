class Car:
    def __init__(self ,brand,model):
        self.brand=brand
        self.model=model
    def start (self):
        return "vroom"
    def full_name(self):
        print(f'the brand of car is {self.brand} and model is {self.model}')


my_car=Car("telsa","x34738dfdj")

my_car.full_name()


