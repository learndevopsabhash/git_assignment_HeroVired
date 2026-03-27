import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width


if __name__ == "__main__":
    calculator = GeometryCalculator()

    # TODO: circle
    # radius = 5
    # print(f"Circle Area = {calculator.calculate_circle_area(radius)}")

    # TODO: rectangle
    # length = 10
    # width = 6
    # print(f"Rectangle Area = {calculator.calculate_rectangle_area(length, width)}")
