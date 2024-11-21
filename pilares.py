# Exemplo de herança
print('\nInheritance example:')
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def to_walk(self):
        print(f'the {self.name} animal to walked.')
        return

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return 'au, au'
    
class Cat(Animal):
    def make_sound(self):
        return 'miau'
    
dog = Dog(name = 'Rex')
cat = Cat(name = 'Felix')

print('\nExample of polymorphism')

animals = [dog, cat]

for animal in animals:
    print(f'{animal.name} does: {animal.make_sound()}')

print('\nEncapsulation example:')
class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance # Atributo privado, colocar 2 underlines

    def deposit(self, value): # Depositar valor
        if value > 0:
            self.__balance += value

    def withdraw(self, value): # Sacar valor
        if value > 0 and value <= self.__balance:
            self.__balance -= value

    def consult(self):
        return self.__balance
    
# iniciando saldo
account = BankAccount(balance = 1000)
print(f'Bank account balance: {account.consult()}')

# depositando dinheiro
account.deposit(value = 500)
print(f'Bank account balance: {account.consult()}')

# sacando dinheiro
account.withdraw(value = 200)
print(f'Bank account balance: {account.consult()}')

# criando nova conta bancária
account_mariana = BankAccount(balance = 50)
print(f'Bank account balance: {account_mariana.consult()}')

print('\nAbstraction example:')
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Car(Vehicle):
    def __init__(self) -> None:
        pass

    def connect(self):
        # ligação do carro
        return 'Car connect using key'
    
    def disconnect(self):
        # desligando o carro
        return 'Car disconnect using key'

car_yellow = Car()
print(car_yellow.connect())
print(car_yellow.disconnect())