class Shape:
    def __init__(self, saving):
        self.saving = saving

    def show(self):
        self.information = f'{self.__class__.__name__}: {self.__dict__} \n'
        return self.information

    def save(self):
        with open(self.saving, 'a') as f:
            f.writelines(self.information)

    def load(self):
        with open(self.saving, 'r') as f:
            return f.read()


class Square(Shape):
    def __init__(self, saving, coordinate_x, coordinate_y, lenght):
        super().__init__(saving)
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.lenght = lenght

    def __str__(self):
        return f'{super().show()}'


square = Square('MyFigure', 10, 10, 40)
print(square)
square.save()

#

class Rectangle(Shape):
    def __init__(self, saving, coordinate_x, coordinate_y, weight, height):
        super().__init__(saving)
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.weight = weight
        self.height = height

    def __str__(self):
        return f'{super().show()}'


rectangle = Rectangle('MyFigure', 30, 30, 10, 30)
print(rectangle)
rectangle.save()

class Circle(Shape):
    def __init__(self, saving, coordinate_x, coordinate_y, radius):
        super().__init__(saving)
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius

    def __str__(self):
        return f'{super().show()}'


circle = Circle('MyFigure',50, 50, 10)
print(circle)
circle.save()


class Ellipse(Shape):
    def __init__(self, saving, coordinate_x, coordinate_y, weight, height):
        super().__init__(saving)
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.weight = weight
        self.height = height

    def __str__(self):
        return super().show()


ellips = Ellipse('MyFigure', 20, 20, 30, 40)
print(ellips)
ellips.save()

print(ellips.load())
