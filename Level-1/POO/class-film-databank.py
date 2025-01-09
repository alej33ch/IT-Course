from datetime import datetime

class Movie:
    def __init__(self, title, director, year, genre,rating):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = rating
        #self.rating = None

    def show_info(self):
        print(f"Title: {self.title}\nDirector: {self.director}\nYear: {self.year}\nGenre: {self.genre}\nRating:{self.rating}")

    def rate(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
            print(f"Rating: {self.rating}")
        else:
            print("The rating must be between 1 and 5.")

    def is_new(self):
        current_year = datetime.now().year
        if self.year == current_year:
            return True
        return False


movie_1 = Movie("Alejandro and His Death", "Pedro Escobar", 2025, "Action", 5)
movie_2 = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi",3)
movie_3 = Movie("The Dark Knight", "Christopher Nolan", 2008, "Action",4)
movie_4 = Movie("Titanic", "James Cameron", 1997, "Romance",3)
movie_5 = Movie("The Matrix", "Wachowski Sisters", 1999, "Sci-Fi",5 )
movie_6 = Movie("Avatar", "James Cameron", 2009, "Sci-Fi", 3)
movie_7 = Movie("The Godfather", "Francis Ford Coppola", 1972, "Crime",5)
movie_8 = Movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama",3 )
movie_9 = Movie("Forrest Gump", "Robert Zemeckis", 1994, "Drama", 3)
movie_10 = Movie("Gladiator", "Ridley Scott", 2000, "Action", 2)
movie_11 = Movie("The Lion King", "Roger Allers, Rob Minkoff", 1994, "Animation", 2)
movie_12 = Movie("Pulp Fiction", "Quentin Tarantino", 1994, "Crime",5 )
movie_13 = Movie("Star Wars: A New Hope", "George Lucas", 1977, "Adventure", 2)
movie_14 = Movie("Jurassic Park", "Steven Spielberg", 1993, "Adventure", 1)
movie_15 = Movie("The Silence of the Lambs", "Jonathan Demme", 1991, "Thriller", 2)


movie_1.show_info()


""""
movie_3.rate(3)
if movie_3.is_new():
    print(f"The movie '{movie_3.title}' is new.")
else:
    print(f"The movie '{movie_3.title}' is not new.")
"""