class Car:
    def __init__(self ,brand,model):
        self.brand=brand
        self.model=model
    def start (self):
        return "vroom"
    def full_name(self):
            print(f'the brand of car is {self.brand} and model is {self.model}')





class ElectricCar(Car):
    def __init__(self,batterysize,brand,model):
        super().__init__(brand,model)
        self.battery=batterysize


my_electric_car=ElectricCar(100,"telsa","x34738dfdj")

my_electric_car.full_name()
print(my_electric_car.battery)





