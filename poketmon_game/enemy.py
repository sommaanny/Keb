class Anemy:
    def __init__(self):
        self.__hp__ = 100
        self.__basicDamage__ = 20
    
    def getBasicDamage(self):
        return self.__basicDamage__
    
    def getHP(self):
        return self.__hp__
    
    def attack(self):
        print(f"{self.__name__} Attack!")
    
    def damage(self, n):
        self.__hp__ -= n
    
class Meowth(Anemy):    # 1번
    def __init__(self):
        super().__init__()
        self.__name__ = "Meowth"
        print("I'm Meowth(냐옹이)!")


class Magikarp(Anemy):    # 2번
    def __init__(self):
        super().__init__()
        self.__name__ = "Magikarp"
        self.__hp__ = 150
        self.__basicDamage__ = 40
        print("I'm Magikarp(잉어킹)!")
    
    def skill(self):
        print("Splash!")
        return 80


class Dragonite(Anemy):    # 3번
    def __init__(self):
        super().__init__()
        self.__name__ = "Dragonite"
        self.__hp__ = 300
        self.__basicDamage__ = 60
        print("I'm Dragonite(망나뇽)!")
    
    def skill(self):
        print("Fire Punch!")
        return 150

