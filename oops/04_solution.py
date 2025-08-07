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




my_car=Car("telsa","x34738dfdj")

print(my_car.get_brand())
print(my_car.__brand)

