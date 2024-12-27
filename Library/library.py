from Book.book import Book


class Library:
    def __init__(self):
        self.books = []
        self.avaiable_books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
