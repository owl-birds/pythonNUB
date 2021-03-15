import math
def sqrt(num):
    r = num
    precision = 10 ** (-10)
    while abs(num - r * r) > precision:
        r = (r + num / r) / 2
    return r
print(math.sqrt(3))
print(sqrt(3))

## Exercises OOP
# 1
class Line():
    def __init__(self, coor1, coor2):
        # coor expect a list of two axis
        self.coor1 = coor1
        self.coor2 = coor2
    def __str__(self):
        return "coor1 : {}\ncoor2 : {}".format(self.coor1,self.coor2)
    def distance(self):
        return sqrt((self.coor1[0]-self.coor2[0])**2+(self.coor1[1]-self.coor2[1])**2)
    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
line1 = Line([3, 2], [9, 7])
line2 = Line([3,2],[4,5])
print(line1)
print(line1.distance())
print(line2.slope())
# 2
class Cylinder():
    from math import pi
    #pi = pi
    # Constructor
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    def __str__(self):
        return "radius : {}\nheight : {}".format(self.radius,self.height)
    # METHODS
    def volume(self):
        return (Cylinder.pi * (self.radius ** 2)) * self.height
    def surfaceArea(self):
        return (2 * (Cylinder.pi * (self.radius ** 2))) + ((2 * Cylinder.pi * self.radius) * self.height)
cylinder1 = Cylinder(2,3)        
print(cylinder1)
print(cylinder1.volume())
print(cylinder1.surfaceArea())