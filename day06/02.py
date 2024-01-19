class Poketmon:
    def __init__(self, leg):
        self.leg = leg
    def getLeg(self):
        return self.leg
    
pch = Poketmon(4)
print(pch.getLeg())