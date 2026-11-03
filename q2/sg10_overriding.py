class Animal: # Creates the parent class
    def __init__(self, name): # The constructor method that creates the attributes
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.") # Creates an eat method that is common to all animals

    def make_sound(self):
        print(f"{self.name} makes a sound.") # Creates a making sound method that is common to all animals

class Lion(Animal): # Creates the child class that inherits from the parent class
    def __init__(self, name): # The constructor method that creates the attributes
        super().__init__(name) # Calls the constructor of the parent class
    def make_sound(self): # Overriding the make_sound method of the parent class
        print(f"{self.name} roars loudly!")
    def eat(self): # Overriding the eat method of the parent class
        print(f"{self.name} eats fresh meat.")

class Elephant(Animal): # Creates the child class that inherits from the parent class
    def __init__(self, name): # The constructor method that creates the attributes
        super().__init__(name) # Calls the constructor of the parent class
    def make_sound(self): # Overriding the make_sound method of the parent class
        print(f"{self.name} trumpets!")
    def eat(self): # Overriding the eat method of the parent class
        print(f"{self.name} eats grass and fruits.")

class Monkey(Animal): # Creates the child class that inherits from the parent class
    def __init__(self, name): # The constructor method that creates the attributes
        super().__init__(name) # Calls the constructor of the parent class
    def make_sound(self): # Overriding the make_sound method of the parent class
        print(f"{self.name} chatters!")
    def eat(self): # Overriding the eat method of the parent class
        print(f"{self.name} eats bananas.")

# Creates objects of the child classes
lion = Lion("Simba") 
elephant = Elephant("Dumbo")
monkey = Monkey("George")

# Calls the methods of the child classes and prints the output
lion.make_sound() # Calls the overridden make_sound method of the Lion class
lion.eat() # Calls the overridden eat method of the Lion class
print("-----") # Prints a separator
elephant.make_sound() # Calls the overridden make_sound method of the Elephant class
elephant.eat() # Calls the overridden eat method of the Elephant class
print("-----") # Prints a separator
monkey.make_sound() # Calls the overridden make_sound method of the Monkey class
monkey.eat() # Calls the overridden eat method of the Monkey class
print("-----") # Prints a separator
