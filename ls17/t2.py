class Airplane:
    def __init__(self, plane_type, max_passengers):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        

    def __eq__(self, other):
        return self.plane_type == other.plane_type


    def __iadd__(self, value):
        self.max_passengers += value
        return self


    def __isub__(self, value):
        self.max_passengers -= value
        return self


    def __lt__(self, other):
        return self.max_passengers < other.max_passengers


    def __le__(self, other):
        return self.max_passengers <= other.max_passengers


    def __gt__(self, other):
        return self.max_passengers > other.max_passengers


    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers


    def __str__(self):
        return f"Airplane type: {self.plane_type}, Max passengers: {self.max_passengers}"


plane1 = Airplane("Boeing 747", 400)
plane2 = Airplane("Airbus A320", 200)

print(plane1 == plane2)  

plane1 += 50
plane2 -= 30

print(plane1) 
print(plane2)  

print(plane1 > plane2)  
print(plane1 <= plane2)  