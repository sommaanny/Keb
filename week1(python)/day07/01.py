class Fruit:
    color = 'red'

blueberry = Fruit()
cherry = Fruit()
print(blueberry.color)
print(cherry.color)
print(Fruit.color)
print(id(blueberry), id(cherry), id(Fruit))
Fruit.color = 'blue'
print(blueberry.color)
print(cherry.color)
print(Fruit.color)
print(id(blueberry), id(cherry), id(Fruit))
print()

class A:
    count = 0
    def __init__(self):
        A.count += 1
    @classmethod
    def kids(self):
        print(A.count)

first = A()
second = A()
A.kids()

class CoyoteWeapon:
    @staticmethod
    def commercial():
        print("test")

CoyoteWeapon.commercial()

class Word:
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
print(first == second)