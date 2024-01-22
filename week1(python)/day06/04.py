class Circle:
    def __init__(self, radius):
        self.__radius = radius
    @property
    def diameter(self):
        return 2 * self.__radius
    
c = Circle(5)
print(c.diameter)
