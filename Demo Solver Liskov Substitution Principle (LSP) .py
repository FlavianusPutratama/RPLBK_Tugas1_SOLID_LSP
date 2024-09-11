# Superclass Shape (bentuk umum)
class Shape:
    def get_area(self):
        raise NotImplementedError("This method should be overridden")

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

# Subclass Square
class Square(Shape):
    def __init__(self, side):
        self._side = side

    def set_side(self, side):
        self._side = side

    def get_area(self):
        return self._side * self._side

# Fungsi untuk menghitung area dari objek Shape
def calculate_area(shape: Shape):
    print(f"Area: {shape.get_area()}")

# Testing
rect = Rectangle(5, 10)
calculate_area(rect)  # Output: Area: 50

square = Square(5)
calculate_area(square)  # Output: Area: 25
