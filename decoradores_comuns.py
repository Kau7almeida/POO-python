# @classmethod
# @staticmethod

class MyClass:
    value = 10 # atributo de classe
    def __init__(self, name) -> None:
        self.name = name # atributo da instância

    # requer instancia para ser chamado
    def method_instance(self):
        return f'Instance method called {self.name}'
    
    @classmethod
    def method_class(cls):
        return f'Class method called is value = {cls.value}'

    @staticmethod
    def method_static():
        return 'Static method called'
    
obj = MyClass(name = 'Example class')
print(obj.method_instance())
print(MyClass.value)
print(MyClass.method_class())
print(MyClass.method_static())

class Car:
    def __init__(self, marca, model, year) -> None:
        self.marca = marca
        self.model = model
        self.year = year

    @classmethod
    def create_car(cls, config):
        marca, model, year = config.split(',')
        return cls(marca, model, int(year))
    
config1 = 'Toyota, Corolla, 2022'
car1 = Car.create_car(config1)
print(f'Marca: {car1.marca}\nModel: {car1.model}\nYear: {car1.year}')

class Math:
    @staticmethod
    def somar(a, b):
        return a + b
    
print(Math.somar(a = 2, b = 5))