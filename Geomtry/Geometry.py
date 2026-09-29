class Square:
    def __init__(self, length):
        self.length = length
        
    def area(self):
        area = self.length ** 2
        return area
        
    def perimeter(self):
        perimeter = 4 * self.length
        return perimeter

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def is_valid(self):
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
            return "Exists"
        return "Does not exist"
        
    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter
        
    def area(self):
        p = self.perimeter() / 2
        area = (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5
        return area

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        return circumference
        
    def area(self):
        area = 3.14 * (self.radius ** 2)
        return area
