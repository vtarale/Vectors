import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_mag(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def set_mag(self, new_mag):
        self.x = self.x * new_mag / self.get_mag()
        self.y = self.y * new_mag / self.get_mag()

    def sub(self, vector):
        self.x = self.x - vector.x
        self.y = self.y - vector.x
    
    def norm(self):
        self.x = self.x * 1 / self.get_mag()
        self.y = self.y * 1 / self.get_mag()

    def add(self, vector):
        self.x = self.x + vector.x
        self.y = self.y + vector.x

    def __sub__(self, vector):
        self.x = self.x - vector.x
        self.y = self.y - vector.x
    
    def __add__(self, vector):
        self.x = self.x + vector.x
        self.y = self.y + vector.x

    def dot(self, vector):
        dot = self.x(vector.x) + self.y(vector.y)
        return dot
