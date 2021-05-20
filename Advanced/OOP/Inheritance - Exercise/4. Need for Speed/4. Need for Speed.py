class Vehicle:

    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, km):
        needed_fuel = km * self.fuel_consumption

        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel




class Car(Vehicle):

    DEFAULT_FUEL_CONSUMPTION = 3.00

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class FamilyCar(Car):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class SportCar(Car):

    DEFAULT_FUEL_CONSUMPTION = 10.00

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)



class Motorcycle(Vehicle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8.00

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)



class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

car = Car(100, 2)
sportcar = SportCar(2, 100)
motor = Motorcycle(2, 10)
racemotor = RaceMotorcycle(2, 10)
crossmotor = CrossMotorcycle(2, 10)
print(vehicle.fuel_consumption)
print(car.fuel_consumption)
print(family_car.fuel_consumption)
print(sportcar.fuel_consumption)
print(motor.fuel_consumption)
print(racemotor.fuel_consumption)
print(crossmotor.fuel_consumption)
