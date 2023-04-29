class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side , side)
    def carpma(self):
        return self.length * self.width
# Create a square
square = Square(10)
print(square.carpma())



# Print the square's attributes
print(square.length)  # 10
print(square.width)  # 10
