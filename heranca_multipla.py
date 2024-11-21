class Animal: # classe animal
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        pass

class Mammal(Animal): # classe mamifero que herda animal
    def breastfeed(self):
        return f'{self.name} is breastfeeding.'
    
class Bird(Animal): # classe ave que herda de animal
    def fly(self):
        return f'{self.name} is flying.'

class Bat(Mammal, Bird): # classe morcego que herda de mamifero e ave
    def make_sound(self):
        return 'Bats make ultrasonic sounds'
    
bat = Bat(name = 'Batman')

# acessando métodos da classe base 'Animal'
print('Bat name:', bat.name)
print('Bat sound:', bat.make_sound())

# acessando métodos das classes 'Mamifero e Ave'
print('Bat breastfeeding', bat.breastfeed())
print('Bat flying', bat.fly())