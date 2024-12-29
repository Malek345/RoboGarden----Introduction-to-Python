class Book:
    """
    Class to represent a book with attributes and methods.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Default availability status

    def check_out(self):
        """
        Method to check out the book.
        """
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' by {self.author} has been checked out.")
        else:
            print(f"'{self.title}' by {self.author} is currently unavailable.")

    def return_book(self):
        """
        Method to return the book.
        """
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' by {self.author} has been returned.")
        else:
            print(f"'{self.title}' by {self.author} was not checked out.")

    def display_info(self):
        """
        Method to display book information.
        """
        status = "Available" if self.is_available else "Checked Out"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Library:
    """
    Class to represent a library catalogue system.
    """
    def __init__(self):
        self.catalogue = []

    def add_book(self, title, author):
        """
        Method to add a new book to the library.
        """
        book = Book(title, author)
        self.catalogue.append(book)
        print(f"Book '{title}' by {author} has been added to the catalogue.")

    def display_catalogue(self):
        """
        Method to display all books in the catalogue.
        """
        if not self.catalogue:
            print("The library catalogue is empty.")
        else:
            print("Library Catalogue:")
            for book in self.catalogue:
                book.display_info()
            print("-" * 40)

    def find_book(self, title):
        """
        Method to find a book by title in the catalogue.
        """
        for book in self.catalogue:
            if book.title.lower() == title.lower():
                return book
        print(f"Book '{title}' not found in the catalogue.")
        return None


def main():
    # Create the library system
    library = Library()

    # Add books to the library
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # Display the library catalogue
    library.display_catalogue()

    # Check out a book
    book_to_check_out = library.find_book("1984")
    if book_to_check_out:
        book_to_check_out.check_out()

    # Attempt to check out the same book again
    book_to_check_out.check_out()

    # Return the book
    book_to_check_out.return_book()

    # Display the library catalogue again
    library.display_catalogue()

main()
