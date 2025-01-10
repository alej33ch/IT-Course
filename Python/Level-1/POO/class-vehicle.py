class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            return f"The vehicle {self.brand} {self.model} has started."
        else:
            return f"The vehicle {self.brand} {self.model} is already runnig."

    def stop(self):
        if self.running:
            self.running = False
            return f"The vehicle {self.brand} {self.model} has stopped."
        else:
            return f"The vehicle {self.brand} {self.model} is already stopped"

my_car = Vehicle("Toyota", "Corolla")
my_second_car = Vehicle("Porsche", "Cayenne")

print(my_car.stop())
print(my_car.start())
print(my_car.stop())

print(my_second_car.start())
print(my_second_car.stop())
print(my_second_car.start())
print(my_second_car.stop())
