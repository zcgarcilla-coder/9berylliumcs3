class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = int(number_of_pages)

    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages < 0:
            print("Number of pages cannot be negative.")
            return
        self.number_of_pages = int(number_of_pages)

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.number_of_pages}")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = int(issue_number)

    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        if issue_number < 0:
            print("Issue number cannot be negative.")
            return
        self.issue_number = int(issue_number)

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

# Creating first objects
pub1 = Publication("Generic Publication", "John Doe")
book1 = Book("Python Programming", "Jane Smith", 350)
mag1 = Magazine("Tech Monthly", "Alice Johnson", 42)

# Displaying information
print("Publication Information:")
pub1.display_info()
print("\nBook Information:")
book1.set_number_of_pages(400)  # Updating the number of pages
book1.display_info()
print(book1.get_number_of_pages())  # Accessing the number of pages
print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())  # Accessing the issue number

pub2 = Publication("Another Publication", "Emily Davis")
book2 = Book("Data Science Essentials", "Michael Brown", 250)
mag2 = Magazine("Science Weekly", "David Wilson", 15)

# Displaying information for the second set of objects
print("\nPublication Information:")
pub2.display_info()
print("\nBook Information:")
book2.set_number_of_pages(-300)  # P
book2.display_info()
print(book2.get_number_of_pages())  # Accessing the number of pages
print("\nMagazine Information:")
mag2.display_info()
