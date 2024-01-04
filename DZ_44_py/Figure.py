from math import pi


class Figure:
    pass


class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    @property
    def square(self):
        self.squr = self.side1 * self.side2
        return self.squr

    def __int__(self):
        self.squr = self.side1 * self.side2
        return self.squr

    def __str__(self):
        return f'{self.__class__.__name__} square: {self.__int__()}'


rect = Rectangle(5, 10)
print(rect)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    @property
    def square(self):
        return pi * self.radius ** 2

    def __int__(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f'{self.__class__.__name__} square: {self.__int__()}'


print()
circle = Circle(5)
print(circle)


class Riangle(Figure):
    def __init__(self, catheter1, catheter2):
        self.catheter1 = catheter1
        self.catheter2 = catheter2

    @property
    def square(self):
        return (self.catheter1 * self.catheter2) / 2

    def __int__(self):
        return (self.catheter1 * self.catheter2) / 2

    def __str__(self):
        return f'{self.__class__.__name__} square: {self.__int__()}'


print()
riangle = Riangle(5, 10)
print(riangle)


class Trapezoid(Figure):
    def __init__(self, footing1, footing2, height):
        self.footing1 = footing1
        self.footing2 = footing2
        self.height = height

    @property
    def square(self):
        return (self.footing1 + self.footing2) * self.height / 2

    def __int__(self):
        return (self.footing1 + self.footing2) * self.height / 2

    def __str__(self):
        return f'{self.__class__.__name__} square: {self.__int__()}'


print()
trap = Trapezoid(10, 20, 5)
print(trap)
