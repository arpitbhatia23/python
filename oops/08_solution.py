class Car:
    totalcar=0
    def __init__(self ,brand,model):
        self.__brand=brand
        self.__model=model
        Car.totalcar+=1

    def get_brand(self):
         return str(self.__brand.capitalize())
    
    def start (self):
        return "vroom"
    def full_name(self):
            print(f'the brand of car is {self.__brand} and model is {self.__model}')
    def fuel_type(self):
         return "petrol"
    @staticmethod
    def general_description():
        return "car are mean of trasnport"
    @property
    def model(self):
         return self.__model
   
my_car=Car("tata","safari")
# my_car.model="tesla"
print(my_car.model)
