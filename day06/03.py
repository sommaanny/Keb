class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."

class Poketmon:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print("공격합니다.")

class Charizard(Poketmon, FlyingMixin):
    pass

class Gyarados(Poketmon, SwimmingMixin):
    pass



g1 = Gyarados("갸라도스")
g2 = Charizard("리자몽")
print(g1.swim())
print(g2.fly())
Charizard.attack(g2)

