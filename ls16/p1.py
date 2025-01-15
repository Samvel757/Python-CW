class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def display_info(self):
        return f"Устройство: {self.model} (Бренд: {self.brand}, Мощность: {self.power} Вт)"


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_capacity):
        super().__init__(brand, model, power)  
        self.water_capacity = water_capacity

    def make_coffee(self):
        return "Кофе готовится..."

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Объем воды: {self.water_capacity} л"


class Blender(Device):
    def __init__(self, brand, model, power, speed_modes):
        super().__init__(brand, model, power)  
        self.speed_modes = speed_modes

    def blend(self):
        return "Смешивание началось..."

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Режимы скорости: {self.speed_modes}"


class MeatGrinder(Device):
    def __init__(self, brand, model, power, blade_material):
        super().__init__(brand, model, power)
        self.blade_material = blade_material

    def grind_meat(self):
        return "Мясо перемалывается..."

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Материал лезвий: {self.blade_material}"



coffee_machine = CoffeeMachine("Philips", "LatteGo", 1500, 1.8)
blender = Blender("Bosch", "VitaBoost", 1200, 5)
meat_grinder = MeatGrinder("Moulinex", "HV8", 2000, "нержавеющая сталь")

print(coffee_machine.display_info())
print(coffee_machine.make_coffee())

print(blender.display_info())
print(blender.blend())

print(meat_grinder.display_info())
print(meat_grinder.grind_meat())