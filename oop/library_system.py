class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_details(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __str__(self):
        return self.get_details()


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, published in {self.year}, File Size: {self.file_size}KB"

    def __str__(self):
        return self.get_details()


class PrintBook(Book):
    def __init__(self, title, author, year, page_count):
        super().__init__(title, author, year)
        self.page_count = page_count

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, published in {self.year}, Page Count: {self.page_count}"

    def __str__(self):
        return self.get_details()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
