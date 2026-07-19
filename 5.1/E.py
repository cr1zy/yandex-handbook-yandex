class Rectangle():

    def __init__(self, a, c):
        self.x1 = a[0]
        self.y1 = a[1]
        self.x2 = c[0]
        self.y2 = c[1]

    def perimeter(self):
        return round((abs(self.x2 - self.x1) + abs(self.y2 - self.y1)) * 2, 2)
    
    def area(self):
        return round((abs(self.x2 - self.x1) * abs(self.y2 - self.y1)), 2)
    
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
