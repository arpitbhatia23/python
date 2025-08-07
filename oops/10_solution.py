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


class Battery:
     def battery_info(self):
          return "this  is battery"

class Engine:
     def engine_info(self):
            return "this is engine "
          

class ElectricEngine(Battery,Engine,Car):
        pass
my_new_tessla=ElectricEngine("telsa","engine")

print(my_new_tessla.engine_info())
print(my_new_tessla.battery_info())