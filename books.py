from abc import ABC, abstractmethod


class Book(ABC):

    def __init__(self, title: str, price: str):
        self.title = title
        self.price = price
     
    @abstractmethod
    def get_info(self) -> str:
        pass

    @abstractmethod
    def set_dict(self) -> dict:
        pass

    def get_title(self) -> str:
        return f"{self.title}"

    def get_price(self) -> str:
        return f"{self.price}"



class BookshopWebiteBook(Book):
    
    bookshop_books = {0: {"title": "", "price": ""}}

    def __init__(self, book_number: int, title: str, price: str):
        super().__init__(title, price)
        self.book_number = book_number

    def get_info(self) -> str:
        return f"{self.title} | {self.price} - In Stock"

    def set_dict(self) -> dict:
        self.bookshop_books[self.book_number] = {}
        self.bookshop_books[self.book_number]["title"] = self.title
        self.bookshop_books[self.book_number]["price"] = self.price
        return self.bookshop_books
    





