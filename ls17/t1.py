class Circle:
    def __init__(self, radius):
        self.radius = radius


    def __eq__(self, other):
        return self.radius == other.radius
        

    def __lt__(self, other):
        return self.radius < other.radius


    def __gt__(self, other):
        return self.radius > other.radius


    def __add__(self, value):
        return Circle(self.radius + value)


    def __sub__(self, value):
        return Circle(self.radius - value)


    def __str__(self):
        return f"Circle with radius: {self.radius}"


circle1 = Circle(5)
circle2 = Circle(10)

print(circle1 == circle2)  

print(circle1 < circle2)  

circle3 = circle1 + 3
circle4 = circle2 - 4

print(circle3)  
print(circle4)  
