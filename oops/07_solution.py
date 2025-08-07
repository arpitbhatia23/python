#  static

class Car:
    totalcar=0
    def __init__(self ,brand,model):
        self.__brand=brand
        self.model=model
        Car.totalcar+=1

    def get_brand(self):
         return str(self.__brand.capitalize())
    
    def start (self):
        return "vroom"
    def full_name(self):
            print(f'the brand of car is {self.brand} and model is {self.model}')
    def fuel_type(self):
         return "petrol"
    @staticmethod
    def general_description():
        return "car are mean of trasnport"

my_car=Car("telsa","x34738dfdj")


print(Car.general_description())
