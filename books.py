from abc import ABC, abstractmethod


class Book(ABC):

    book_number = 0
    location = None
    bookshop_books = {}
    
    def get_info(self, book_number) -> str:
        title = Book.bookshop_books[book_number]["title"]
        price = Book.bookshop_books[book_number]["price"]
        location = Book.bookshop_books[book_number]["location"]
        qty = Book.bookshop_books[book_number]["qty"]
        print(f"{title}\n{price}\n{location}\n{qty}")

    def get_title(self, book_number) -> str:
        title = self.bookshop_books[book_number]["title"]
        return f"Book title: {title}"
    
    def get_price(self, book_number) -> str:
        price = self.bookshop_books[book_number]["price"]
        return f"Book price: {price}"

    def remove_book(self, book_number) -> str:
        Book.bookshop_books.pop(book_number)
        print(Book.bookshop_books)

    def add_book(self, title, price) -> dict:
        Book.book_number += 1
        Book.bookshop_books[self.book_number] = {}
        Book.bookshop_books[self.book_number]["title"] = title
        Book.bookshop_books[self.book_number]["price"] = price
        Book.bookshop_books[self.book_number]["location"] = self.location
        Book.bookshop_books[self.book_number]["qty"] = 0
        print(f"Book Number: {self.book_number}\n{title}\n{price}\nAdded to the system")

    def show_all_books_by_store(self):
        for book_number, _ in self.bookshop_books.items():
            if self.bookshop_books[book_number]["location"] == self.location:
                print(self.bookshop_books[book_number])

    @abstractmethod
    def set_qty(self, book_number, qty):
        pass

class BookshopWebiteBook(Book):

    location = "Online Store"

    def set_qty(self, book_number, qty):
        self.bookshop_books[book_number]["qty"] = qty
        print(f"{self.bookshop_books[book_number]['title']} - Website stock amended to {qty}")
        

class BookshopStoreBook(Book):

    location = "Store"

    def set_qty(self, book_number, qty):
        self.bookshop_books[book_number]["qty"] = qty
        print(f"{self.bookshop_books[book_number]['title']} - Store stock amended to {qty}")



