# Class - Template
class Library:

    # Initial state of the object
    def __init__(self, title, author, year, available):
        self.title = title
        self.author = author
        self.publication_year = year
        self.available = available

    def lend(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' has been lent out.")
        else:
            print(f"The book '{self.title}' is currently not available for lending.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' has been returned and is now available.")
        else:
            print(f"The book '{self.title}' was already available.")

    def show_information(self):
        status = "Available" if self.available else "Not available"
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}\nStatus: {status}\n\nThank you for your inquiry.\nBest regards, Your Library.")

# Create books == books library
book1 = Library("Death Will Come", "Alejadro Ariza", 1990, True)
book2 = Library("One Hundred Years of Solitude", "Gabriel García Márquez", 1967, True)
book3 = Library("Don Quixote", "Miguel de Cervantes", 1605, True)
book4 = Library("The Little Prince", "Antoine de Saint-Exupéry", 1943, False)
book5 = Library("1984", "George Orwell", 1949, True)
book6 = Library("Chronicle of a Death Foretold", "Gabriel García Márquez", 1981, True)
book7 = Library("The Lord of the Rings", "J.R.R. Tolkien", 1954, False)
book8 = Library("Pride and Prejudice", "Jane Austen", 1813, True)
book9 = Library("To Kill a Mockingbird", "Harper Lee", 1960, False)
book10 = Library("Hopscotch", "Julio Cortázar", 1963, True)
book11 = Library("The Picture of Dorian Gray", "Oscar Wilde", 1890, False)
book12 = Library("Ulysses", "James Joyce", 1922, True)
book13 = Library("The Odyssey", "Homer", -800, True)
book14 = Library("Les Misérables", "Victor Hugo", 1862, False)
book15 = Library("The Divine Comedy", "Dante Alighieri", 1320, True)
book16 = Library("Fahrenheit 451", "Ray Bradbury", 1953, False)

# Test book actions
book10.show_information()
book10.lend()
book10.lend()
book10.return_book()
book10.lend()
