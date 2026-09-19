class Genre:
  def __init__(self, genre_type, genre_desc):
    self.attribute1 = genre_type
    self.attribute2 = genre_desc
    self.related_objects = []

  def add_object(self, object_reference):
    self.related_objects.append(object_reference)

  def __str__(self):
    return f"Genre: {self.attribute1}, Description: {self.attribute2}"
class Movies:
    def __init__(self, title, director, genre_type, genre_desc, rating):
        self.attribute1 = title
        self.attribute2 = director
        self.genre = Genre(genre_type, genre_desc)
        self.attribute3 = rating

    def __str__(self):
      return f"Title: {self.attribute1}, Director: {self.attribute2}, Genre: {self.genre.attribute1}, Description: {self.genre.attribute2}, Rating: {self.attribute3}"

def greet(name):
    print(f"Hello, {name}! Welcome to the Movie Inventory System.")
    print("Welcome to the movie inventory system!")

greet("User")
  
inventory = []

def add_movie():
  title = input("Enter the title of the movie: ")
  director = input("Enter the director of the movie: ")
  genre_type = input("Enter the genre of the movie: ")
  genre_desc = input("Enter the description of the genre: ")
  rating = input("Enter the rating of the movie: ")
  movie = Movies(title, director, genre_type, genre_desc, rating)
  movie.genre.add_object(movie)
  inventory.append(movie)
  return inventory

def display_movies():
  if len(inventory) == 0:
    print("No movies in the inventory.")
  else:
    for i, movie in enumerate(inventory):
      print(f"\nMovie {i+1}:")
      print(f"Title: {movie.attribute1}")
      print(f"Director: {movie.attribute2}")
      print(f"Genre: {movie.genre.attribute1}")
      print(f"Description: {movie.genre.attribute2}")
      print(f"Rating: {movie.attribute3}")
  return inventory
        
def update_movie():
  if len(inventory) == 0:
    print("No movies in the inventory.")
  else:
    display_movies()
    movie_index = int(input("Enter the number of the movie you want to update: ")) - 1
    if movie_index < 0 or movie_index >= len(inventory):
      print("Invalid index. Please try again.")
    else:
      title = (input("Enter the new title of the movie: "))
      director = (input("Enter the new director of the movie: "))
      genre_type = (input("Enter the new genre of the movie: "))
      genre_desc = (input("Enter the new description of the genre: "))
      rating = (input("Enter the new rating of the movie: "))
      inventory[movie_index].attribute1 = title
      inventory[movie_index].attribute2 = director
      inventory[movie_index].genre = Genre(genre_type, genre_desc)
      inventory[movie_index].attribute3 = int(rating)
      print("Movie updated successfully.")
  return inventory

def delete_movie():
  if len(inventory) == 0:
    print("No movies in the inventory.")
  else:
    display_movies()
    movie_index = int(input("Enter the number of the movie you want to delete: ")) - 1
    if movie_index < 0 or movie_index >= len(inventory):
      print("Invalid index. Please try again.")
    else:
      del inventory[movie_index]
      print("Movie deleted successfully.")
  return inventory

while True:
  print("\n1. Add movie.")
  print("2. Display movie/s.")
  print("3. Update properties of a movie.")
  print("4. Delete a movie.")
  print("5. Exit.")
    
  choice = int(input("Enter your choice (*must be only the number): "))

  if choice == 1:
    add_movie()
  elif choice == 2:
    display_movies()
  elif choice == 3:
    update_movie()
  elif choice == 4:
    delete_movie()
  elif choice == 5:
    break
  else:
    print("Invalid choice. Please try again.")


print("--- BEFORE RELATIONSHIP ---")
movie = Movies("Inception", "Christopher Nolan", "Science Fiction", "A genre that uses speculative, fictional science-based depictions of phenomena.", 8.8)
scifi_genre = Genre("Science Fiction", "A genre that uses speculative, fictional science-based depictions of phenomena.")
thriller_genre = Genre("Thriller", "A genre that focuses on tension, suspense, and excitement.")
action_genre = Genre("Action", "A genre that focuses on physical action and adventure.")
print(f"Movie: {movie}")
print(f"Genre 1: {scifi_genre}")
print(f"Genre 2: {thriller_genre}")
print(f"Genre 3: {action_genre}")
print("--- BUILDING RELATIONSHIP ---")
movie.genre.add_object(scifi_genre)
movie.genre.add_object(thriller_genre)
movie.genre.add_object(action_genre)
print("--- AFTER RELATIONSHIP ---")
print(f"Movie: {movie.attribute1}")
print(f"Director: {movie.attribute2}")
print(f"Genre: {movie.genre.attribute1}")
print(f"Description: {movie.genre.attribute2}")
print(f"Rating: {movie.attribute3}")
print("Related object(s):")
for genre in movie.genre.related_objects:
    print(f" - {genre}")
