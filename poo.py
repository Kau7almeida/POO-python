# POO - programação orientada a objeto / classes e objetos

# Classe exemplo
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greetings(self):
        return f'Hello, my name is {self.name} and i have {self.age} years.'

# Objetos
person1 = Person('Kaua', 18)
message = person1.greetings()
print(message)

person2 = Person('Mariana', 17)
message = person2.greetings()
print(message)