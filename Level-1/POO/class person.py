class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def greet(self):
        return f"Hello, my name is {self.name} and i am {self.age} years old and this is my phone number {self.phone} ."


person1 = Person("Alejandro", 34, "+41 79 953 24 52")
person2 = Person("Rene", 42, "+41 79 511 24 52")
person3 = Person("Sonja", 45, "+41 79 521 55 52")

print(person1.greet())
