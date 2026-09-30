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
    def __init__(self, title, director, genre_types, genre_descs, rating):
        self.attribute1 = title
        self.attribute2 = director
        self.attribute3 = rating

        self.genres = []
        for g_type, g_desc in zip(genre_types, genre_descs):
            genre_obj = Genre(g_type.strip(), g_desc.strip())
            self.genres.append(genre_obj)
            genre_obj.add_object(self)

    def __str__(self):
      genre_str = ", ".join([f"{genre.attribute1} ({genre.attribute2})" for genre in self.genres])
      return f"Title: {self.attribute1}, Director: {self.attribute2}, Genres: {genre_str}, Rating: {self.attribute3}"

def greet(name):
    print(f"Hello, {name}! Welcome to the Movie Inventory System.")
    print("Welcome to the movie inventory system!")

greet("User")
  
inventory = []

def add_movie():
  title = input("Enter the title of the movie: ")
  director = input("Enter the director of the movie: ")
  genre_input = input("Enter the genres of the movie (comma-separated): ")
  desc_input = input("Enter the descriptions of the genres (comma-separated): ")
  genre_types = [g.strip() for g in genre_input.split(",")]
  genre_descs = [d.strip() for d in desc_input.split(",")]
  while len(genre_descs) < len(genre_types):
    genre_descs.append("No description provided.")
  rating = input("Enter the rating of the movie: ")
  movie = Movies(title, director, genre_types, genre_descs, rating)
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
      print(f"Genres: ")
      for genre in movie.genres:
        print(f"  - {genre.attribute1} ({genre.attribute2})")
      print(f"Rating: {movie.attribute3}")
  return inventory
        
def update_movie():
  if len(inventory) == 0:
    print("No movies in the inventory.")
  else:
    display_movies()
    try:
      movie_index = int(input("Enter the number of the movie you want to update: ")) - 1
    except ValueError:
      print("Invalid input. Please enter a number.")
      return inventory
    if movie_index < 0 or movie_index >= len(inventory):
      print("Invalid index. Please try again.")
    else:
      title = (input("Enter the new title of the movie: "))
      director = (input("Enter the new director of the movie: "))
      genre_input = (input("Enter the new genres of the movie (comma-separated): "))
      desc_input = (input("Enter the new descriptions of the genres (comma-separated): "))
      genre_types = [g.strip() for g in genre_input.split(",")]
      genre_descs = [d.strip() for d in desc_input.split(",")]
      while len(genre_descs) < len(genre_types):
        genre_descs.append("No description provided.")
      rating = (input("Enter the new rating of the movie: "))
      inventory[movie_index].attribute1 = title
      inventory[movie_index].attribute2 = director
      updated_genres = []
      for g_type, g_desc in zip(genre_types, genre_descs):
        genre_obj = Genre(g_type.strip(), g_desc.strip())
        updated_genres.append(genre_obj)
        genre_obj.add_object(inventory[movie_index])
      inventory[movie_index].genres = updated_genres
      inventory[movie_index].attribute3 = int(rating)
      print("Movie updated successfully.")
  return inventory

def delete_movie():
  if len(inventory) == 0:
    print("No movies in the inventory.")
  else:
    display_movies()
    try:
      movie_index = int(input("Enter the number of the movie you want to delete: ")) - 1
    except ValueError:
      print("Invalid input. Please enter a number.")
      return inventory
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

  try:  
    choice = int(input("Enter your choice (*must be only the number): "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue

  if choice == 1:
    add_movie()
  elif choice == 2:
    display_movies()
  elif choice == 3:
    update_movie()
  elif choice == 4:
    delete_movie()
  elif choice == 5:
    print("Exiting the program. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")


if len(inventory) > 0:
  print("\nTest 1 - Inheritance: ")
  print("Parent Attribute: ")
  print(f"Movie Genres: {inventory[0].genres[0].attribute1}")
  print("Child Attribute: ")
  print(f"Genre: {inventory[0].genres[0].attribute1}")

if len(inventory) > 0:
  print("Test 2 - Composition: ")
  print("Movie contains Genres: ")
  print(f"{', '.join([f'{genre.attribute1} ({genre.attribute2})' for genre in inventory[0].genres])}")
