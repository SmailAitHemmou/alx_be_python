  #  Implementing Basic OOP for a Library Management System :

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return True
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return True
        print(f"'{title}' was not borrowed.")

    def list_available_books(self):
        for book in self.books:
            if book._is_checked_out:
                print(f"{book.title} by {book.author}")
