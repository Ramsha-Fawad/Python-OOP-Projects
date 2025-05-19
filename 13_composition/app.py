class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")


# Car class using composition
class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine  # Composition: Engine object is part of Car

    def start_car(self):
        print(f"Starting the {self.make} car...")
        self.engine.start()   # Accessing Engine's method via Car

engine1 = Engine(150)
car1 = Car("Toyota", engine1)

car1.start_car()