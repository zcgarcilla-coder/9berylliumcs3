class Genre:
  def __init__(self, ...):
    ...

class Movies:
    def __init__(movie, title, director, genre, rating):
        movie.attribute1 = title
        movie.attribute2 = director
        movie.attribute3 = genre
        movie.__private_attribute = rating

def greet(name):
    print(f"Hello, {name}! Welcome to the Movie Inventory System.")
    print("Welcome to the movie inventory system!")

greet("User")
  
inventory = []

def add_movie():
  title = (input("Enter the title of the movie: "))
  director = (input("Enter the director of the movie: "))
  genre = (input("Enter the genre of the movie: "))
  rating = (input("Enter the rating of the movie: "))
  movie = Movies(title, director, genre, rating)
  inventory.append(movie)
  return inventory
