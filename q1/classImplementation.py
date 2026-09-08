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
    
def display_movies():
  if len(inventory) == 0:
    print("No movies in the inventory.")
  else:
    for i, movie in enumerate(inventory):
      print(f"\nMovie {i+1}:")
      print(f"Title: {movie.attribute1}")
      print(f"Director: {movie.attribute2}")
      print(f"Genre: {movie.attribute3}")
      print(f"Rating: {movie._Movies__private_attribute}")
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
      genre = (input("Enter the new genre of the movie: "))
      rating = (input("Enter the new rating of the movie: "))
      inventory[movie_index].attribute1 = title
      inventory[movie_index].attribute2 = director
      inventory[movie_index].attribute3 = genre
      inventory[movie_index]._Movies__private_attribute = rating
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