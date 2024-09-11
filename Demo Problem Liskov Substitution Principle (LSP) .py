# Superclass Rectangle
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

# Subclass Square yang melanggar LSP
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    # Override set_width agar sisi selalu sama
    def set_width(self, width):
        self._width = self._height = width

    # Override set_height agar sisi selalu sama
    def set_height(self, height):
        self._width = self._height = height

# Fungsi untuk menghitung area dari objek Rectangle
def calculate_area(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    print(f"Area: {rectangle.get_area()}")

# Testing
rect = Rectangle(2, 3)
calculate_area(rect)  # Output: Area: 50 (sesuai dengan panjang dan lebar)

square = Square(5)
calculate_area(square)  # Output: Area: 100 (tidak sesuai dengan yang diharapkan)
