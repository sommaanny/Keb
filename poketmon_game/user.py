class Poketmon:    # 부모클래스
    def __init__(self):
        self.__hp__ = 100
        self.__basicDamage__ = 30
    
    def getHP(self):
        return self.__hp__
    
    def getBasicDamage(self):
        return self.__basicDamage__

    def attack(self):
        print(f"{self.__name__} Attack!")

    def run(self):
        print(f"{self.__name__} Run!")
    
    def damage(self, n):
        self.__hp__ -= n
    

class Pikachu(Poketmon):
    def __init__(self):
        super().__init__()
        self.__name__ = "Pikachu"
        self.__skill__ = "Mega volt"
        print("Pika Pika!")

    def skill(self):
        print(f"{self.__name__} {self.__skill__}!")
        if self.__name__ == "Pikachu":
            return 50
        else:
            return 100
    
    def evolution(self):
        print("Evolution to Raichu!")
        self.__name__ = "Raichu"
        self.__skill__ ="Lightningrod"
        self.__hp__ = 200
        self.__basicDamage__ = 50


class Charmander(Poketmon):
    def __init__(self):
        super().__init__()
        self.__name__ = "Charmander"
        self.__skill__ = "Flamethrower"
        print("Charmander!")

    def skill(self):
        print(f"{self.__name__} {self.__skill__}!")
        if self.__name__ == "Charmander":
            return 50
        else:
            return 100

    def evolution(self):
        print("Evolution to Charizard(리자몽)!")
        self.__name__ = "Charizard"
        self.__skill__ ="Blaze"
        self.__hp__ = 200
        self.__basicDamage__ = 50


class Squirtle(Poketmon):
    def __init__(self):
        super().__init__()
        self.__name__ = "Squirtle"
        self.__skill__ = "Bubble"
        print("Squrtle!")

    def skill(self):
        print(f"{self.__name__} {self.__skill__}!")
        if self.__name__ == "Squirtle":
            return 50
        else:
            return 100
    
    def evolution(self):
        print("Evolution to Blastoise(거북왕)!")
        self.__name__ = "Blastoise"
        self.__skill__ ="Torrent"
        self.__hp__ = 200
        self.__basicDamage__ = 50

