# classes.py
# Implements a Point class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

    # Homework for you
    # Write a method called quadrant
    # return 1 if x >= 0 y >= 0
    # return 2 if x < 0 y >=0
    # return 3 if x < 0 y < 0
    # return 4 if x >= 0 y < 0
    #
    # Example
    # p = Point(1,2)
    # p.quadrant() # Should return 1



