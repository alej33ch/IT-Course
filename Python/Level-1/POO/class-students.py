class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades    

    def average(self):
        return sum(self.grades) / len(self.grades)

    def show_grades(self):
        return f"{self.name}'s grades are: {self.grades}"


student1 = Student("Anna", [85, 90, 78])


print(student1.show_grades())
print(f"{student1.name}'s average is {student1.average():.2f}.")
