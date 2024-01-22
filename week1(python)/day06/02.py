class Bychel:
    def __init__(self, tire, paddel):
        self.hidden_tire = tire
        self.hidden_paddel = paddel
    def getTire(self):
        return self.hidden_tire
    def getPaddel(self):
        return self.hidden_paddel
    def printHello(self):
        print("Hello")
    
class Car(Bychel):
    def __init__(self, tire, paddel, gas):
        super().__init__(tire, paddel)
        self.hidden_gas = gas
    def getGas(self):
        return self.hidden_gas

benz = Car(4, 2, "disel")
print(benz.getTire())
print(benz.getPaddel())
print(benz.getGas())
benz.printHello()
print()
class Animal:
    def says(self):
        return 'I speak'

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())
