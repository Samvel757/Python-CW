class Wheels:
    def __init__(self, count):
        self.count = count 
    def info(self):
        return f"Колеса: {self.count} шт."



class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower  


    def info(self):
        return f"Двигатель: {self.horsepower} л.с."



class Doors:
    def __init__(self, count):
        self.count = count  


    def info(self):
        return f"Двери: {self.count} шт."


class Car(Wheels, Engine, Doors):
    def __init__(self, count_wheels, horsepower, count_doors, brand, model):
        Wheels.__init__(self, count_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, count_doors)
        self.brand = brand  
        self.model = model  


    def info(self):
        base_info = f"Автомобиль: {self.brand} {self.model}"
        return f"{base_info}\n{Wheels.info(self)}\n{Engine.info(self)}\n{Doors.info(self)}"



car = Car(count_wheels=4, horsepower=150, count_doors=4, brand="Toyota", model="Camry")
print(car.info())
