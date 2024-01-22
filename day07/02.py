class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length

class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')
    def __add__(self, other):
        return f'{self.bill.description} + {self.tail.length} + {other.bill.description} + {other.tail.length}'
a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()
print()
b_tail = Tail('short')
b_bill = Bill('noraml red')
duck_b = Duck(b_bill, b_tail)
print(duck + duck_b)
