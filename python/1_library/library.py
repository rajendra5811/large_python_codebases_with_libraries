class Book:
    next_id = 1

    def __init__(self, title, author):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            print(f"{self.title} is already checked out.")
            return False

        self.is_checked_out = True
        print(f"{self.title} has been checked out.")
        return True

    def return_book(self):
        if not self.is_checked_out:
            print(f"{self.title} was not checked out.")
            return False

        self.is_checked_out = False
        print(f"{self.title} has been returned.")
        return True

    def display_info(self):
        status = "Checked out" if self.is_checked_out else "Available"
        print(f"ID: {self.id} | {self.title} by {self.author} | {status}")


class Member:
    max_borrowed_books = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.max_borrowed_books:
            print(f"{self.name} cannot borrow more than 3 books.")
            return False

        if book.check_out():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
            return True

        return False

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"{self.name} did not borrow {book.title}.")
            return False

        if book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
            return True

        return False

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
            return

        print(f"{self.name}'s borrowed books:")
        for book in self.borrowed_books:
            book.display_info()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} was added to the library.")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book

        return None

    def lend_book(self, book_id, member):
        book = self.find_book_by_id(book_id)

        if book is None:
            print(f"No book found with ID {book_id}.")
            return False

        return member.borrow_book(book)

    def accept_returned_book(self, book_id, member):
        book = self.find_book_by_id(book_id)

        if book is None:
            print(f"No book found with ID {book_id}.")
            return False

        return member.return_book(book)

    def display_available_books(self):
        available_books = []

        for book in self.books:
            if not book.is_checked_out:
                available_books.append(book)

        if not available_books:
            print("No books are currently available.")
            return

        print("Available books:")
        for book in available_books:
            book.display_info()


library = Library()

book1 = Book("The Frozen", "Ravi Kumar")
book2 = Book("The Fire", "Sagar Sharma")
book3 = Book("Python Basics", "Anita Singh")
book4 = Book("Clean Code", "Robert Martin")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

member1 = Member("Sagar")
member2 = Member("Priya")

library.display_available_books()

library.lend_book(1, member1)
library.lend_book(2, member1)
library.lend_book(3, member1)
library.lend_book(4, member1)

library.lend_book(1, member2)

member1.display_borrowed_books()
library.display_available_books()

library.accept_returned_book(1, member2)
library.accept_returned_book(1, member1)

library.display_available_books()