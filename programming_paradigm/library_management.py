# library_management.py

class Book:
    """A class representing a book with title, author, and checkout status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that holds a collection of books."""
    def __init__(self):
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return  # Successfully checked out
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return  # Successfully returned
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found.")

    def list_available_books(self):
        """Print all available books (not checked out)."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")