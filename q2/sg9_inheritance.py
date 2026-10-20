class Publication:
    def __init__(self, title, author):
        self.title = title # Initializing the title attribute
        self.author = author # Initializing the author attribute

    def get_title(self): # Public method to access the title attribute
        return self.title

    def get_author(self): # Public method to access the author attribute
        return self.author

    def set_title(self, title): # Public method to set the title attribute
        self.title = title

    def set_author(self, author): # Public method to set the author attribute
        self.author = author

    def display_info(self): # Public method to display the information of the publication
        print(f"Title: {self.title}, Author: {self.author}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author) # Calling the constructor of the parent class
        self.number_of_pages = int(number_of_pages) # Initializing the number of pages attribute, makes the property an integer

    def get_number_of_pages(self): # Public method to access the number of pages attribute
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages): # Public method to set the number of pages attribute
        if number_of_pages < 0: # Checks if negative
            print("Number of pages cannot be negative.")
            return
        self.number_of_pages = int(number_of_pages)

    def display_info(self): # Overriding the display_info method to include number of pages
        super().display_info()
        print(f"Number of Pages: {self.number_of_pages}")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author) # Calling the constructor of the parent class
        self.issue_number = int(issue_number) # Initializing the issue number attribute, makes the property an integer

    def get_issue_number(self): # Public method to access the issue number attribute
        return self.issue_number

    def set_issue_number(self, issue_number): # Public method to set the issue number attribute
        if issue_number < 0: # Checks if negative
            print("Issue number cannot be negative.")
            return
        self.issue_number = int(issue_number)

    def display_info(self): # Overriding the display_info method to include issue number
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

# Creating first objects
pub1 = Publication("Generic Publication", "John Doe")
book1 = Book("Python Programming", "Jane Smith", 350)
mag1 = Magazine("Tech Monthly", "Alice Johnson", 42)

# Displaying information for the first set of objects
print("Publication Information:")
pub1.display_info()
print("\nBook Information:")
book1.set_number_of_pages(400)  # Updating the number of pages
book1.display_info()
print(book1.get_number_of_pages())  # Accessing the number of pages
print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())  # Accessing the issue number

# Creating second objects
pub2 = Publication("Another Publication", "Emily Davis")
book2 = Book("Data Science Essentials", "Michael Brown", 250)
mag2 = Magazine("Science Weekly", "David Wilson", 15)

# Displaying information for the second set of objects
print("\nPublication Information:")
pub2.display_info()
print("\nBook Information:")
book2.set_number_of_pages(-300)  # Attempting to set a negative number of pages
book2.display_info()
print(book2.get_number_of_pages())  # Accessing the number of pages
print("\nMagazine Information:")
mag2.display_info()
print(mag2.get_issue_number())  # Accessing the issue number
