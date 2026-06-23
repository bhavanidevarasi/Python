'''
class Book:
    def __init__(self,title,author,isbn,is_available):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_available=True
    def borrow(self):
        if self.is_available:
            self.is_available=False
            return True
        return False
    def return_book(self):
        self.is_available=True
    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print()
        print(f'title : {self.title}')
        print(f'author : {self.author}')
        print(f'isbn : {self.isbn}')
        print(f'status : {self.status}')
class Member:
    def __init__(self,member_id,name,borrowed_books):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=borrowed_books
    def borrow_book()
    '''    

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"

        print("-" * 40)
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"ISBN   : {self.isbn}")
        print(f"Status : {status}")
        print("-" * 40)


class Member:
    MAX_BOOKS = 3

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BOOKS:
            print(f"{self.name} has reached the borrowing limit.")
            return

        if book.borrow():
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed "{book.title}" successfully.')
        else:
            print(f'"{book.title}" is not available.')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f'{self.name} returned "{book.title}" successfully.')
        else:
            print(f'{self.name} did not borrow "{book.title}".')

    def display_borrowed_books(self):
        print(f"\nBorrowed books for {self.name}:")

        if not self.borrowed_books:
            print("No books borrowed.")
            return

        for index, book in enumerate(self.borrowed_books, start=1):
            print(f"{index}. {book.title}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book added: "{book.title}"')

    def register_member(self, member):
        self.members.append(member)
        print(f"Member registered: {member.name}")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_available_books(self):
        print(f"\nAvailable books in {self.name}:")

        available = False

        for book in self.books:
            if book.is_available:
                book.display_info()
                available = True

        if not available:
            print("No books are currently available.")


if __name__ == "__main__":
    library = Library("City Library")

    book1 = Book(
        "Python Crash Course",
        "Eric Matthes",
        "978-1593279288"
    )

    book2 = Book(
        "Clean Code",
        "Robert C. Martin",
        "978-0132350884"
    )

    book3 = Book(
        "Atomic Habits",
        "James Clear",
        "978-1847941831"
    )

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    member1 = Member("M101", "Alice")

    library.register_member(member1)

    library.display_available_books()

    print("\nBorrowing books...")
    member1.borrow_book(book1)
    member1.borrow_book(book2)

    member1.display_borrowed_books()

    library.display_available_books()

    print("\nReturning a book...")
    member1.return_book(book1)

    member1.display_borrowed_books()

    library.display_available_books()