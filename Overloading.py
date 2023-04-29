"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 + p2)

toplam = int.__add__(3, 3)
carpma = int.__mul__(3, 3)
bolme = int.__truediv__(3, 3)
cikarma = int.__sub__(3, 3)
print(toplam)
print(carpma)
print(bolme)
print(cikarma)
"""

class String:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return String(str(self.value) + str(other.value))


s1 = String("Hello")
s2 = String("World")

print(s1 + s2)
