# polymorphgen
class Car:
    def __init__(self ,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
         return str(self.__brand.capitalize())
    
    def start (self):
        return "vroom"
    def full_name(self):
            print(f'the brand of car is {self.brand} and model is {self.model}')
    def fuel_type(self):
         return "petrol"



class ElectricCar(Car):
    def __init__(self,batterysize,brand,model):
        super().__init__(brand,model)
        self.battery=batterysize
    def fuel_type(self):
         return "electric"


my_electric_car=ElectricCar(100,"telsa","x34738dfdj")
my_car=Car("tata","safari")

print(my_car.fuel_type())
print(my_electric_car.fuel_type())