class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def get_info(self):
      return f'Марка {self.make}, модель {self.model}'

car1= Vehicle('bmw','auto')
print(car1.get_info())

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f'Марка {self.make}, модель {self.model}, тип топлива {self.fuel_type}'


car2 = Car('toyota','machine','gaz')
print(car2.get_info())