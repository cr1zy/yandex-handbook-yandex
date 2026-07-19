class Rectangle():

    def __init__(self, a, c):
        self.ax = min(a[0], c[0])
        self.ay = min(a[1], c[1])
        self.cx = max(a[0], c[0])
        self.cy = max(a[1], c[1])
        self.bx = min(a[0], c[0])
        self.by = max(a[1], c[1])
        self.dx = max(a[0], c[0])
        self.dy = min(a[1], c[1])
        self.width, self.height = round(abs(self.ax - self.cx), 2), round(abs(self.ay - self.cy), 2)

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)
    
    
    def area(self):
        return round(self.width * self.height, 2)
    
    def get_pos(self):
        return (min(self.ax, self.bx, self.cx, self.dx), max(self.ay, self.by, self.cy, self.dy))
    
    def get_size(self):
        return (self.width, self.height)
    
    def move(self, dx, dy):
        self.ax += dx
        self.ay += dy
        self.bx += dx
        self.by += dy
        self.cx += dx
        self.cy += dy
        self.dx += dx
        self.dy += dy

    def resize(self, width, height):
        self.width, self.height = width, height



rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())