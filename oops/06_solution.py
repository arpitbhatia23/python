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




safari=Car("tata","safari")

safaritwo=Car("tata","safari")
print(Car.totalcar)