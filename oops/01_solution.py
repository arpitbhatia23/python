class Car:
    def __init__(self ,brand,model):
        self.brand=brand
        self.model=model
    def start (self):
        return "vroom"

my_car=Car("auddi","x100")

print(my_car.start())

my_new_car=Car("tata","corolla")

print(my_new_car.brand)