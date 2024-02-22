class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book

    def add_member(self, member):
        if member.name in self.members:
            raise ValueError("Member with this name already exists.")
        self.members[member.name] = member

    def borrow_book(self, isbn, member_name):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        if member_name not in self.members:
            raise ValueError("Member not found.")

        book = self.books[isbn]
        if book.borrowed:
            raise ValueError("Book is already borrowed.")

        member = self.members[member_name]
        book.borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, isbn, member_name):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        if member_name not in self.members:
            raise ValueError("Member not found.")

        book = self.books[isbn]
        if not book.borrowed:
            raise ValueError("Book was not borrowed.")

        member = self.members[member_name]
        if book not in member.borrowed_books:
            raise ValueError("This member did not borrow this book.")

        book.borrowed = False
        member.borrowed_books.remove(book)

# Example usage
library = Library()
book = Book("1984", "George Orwell", "1234567890")
member = Member("John Doe")
library.add_book(book)
library.add_member(member)
