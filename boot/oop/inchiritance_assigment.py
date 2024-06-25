class Shape:
    def calculate_area(self):
        return 0.0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2


# Test the implementation
shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 4)]
for shape in shapes:
    print("Area of", shape.__class__.__name__, ":", shape.calculate_area())
