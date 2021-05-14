class Rectangle:
    def __init__(self, breadth, length):
        self.b = breadth
        self.l = length

    def area(self):
        return (self.b * self.l)
    
    def perimeter(self):
        return 2*(self.b + self.l)


class Square(Rectangle):
    def __init__(self, side):
        self.s = side
        super().__init__(side, side)
