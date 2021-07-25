from save_to_file import CSVFile
from books import BookshopWebiteBook  
import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Website:

    def __init__(self, url):
        self.url = url
        

    def connect(self):
        res = requests.get(self.url)
        if res.status_code != 200:
            print(f"Error connecting - {res.status_code} status code")
        else:
            print(f"Connection made - {res.status_code} status code")
            return res.text

class WebsiteScraper(ABC):

    def __init__(self, html_response):
        self.html_response = html_response
        self.get_html()

    def get_html(self) -> str:
        self.soup = BeautifulSoup(self.html_response, "lxml")
        return self.soup

    @abstractmethod
    def get_tag(self, tag: str) -> list:
        pass

    def get_href_links(self, tag="href") -> list:
        href_list = []
        for a_tag in self.soup.find_all("a", href=True):
            href_list.append(a_tag[tag].strip())
        return href_list


class BookshopWebsiteScraper(WebsiteScraper):

    def get_tag(self, tag: str) -> list:
        """searches through the html for the tag given"""
        tag_results = []
        for html in self.soup(tag):
            if html.text.strip() == "":
                continue
            tag_results.append(html.text.strip())
        return tag_results
    
    def set_books(self, title: str, price: str) -> dict:
        for book_number, (book_title, book_price) in enumerate(zip(price, title)):
            bookshop_book = BookshopWebiteBook(book_number, book_title, book_price)
            books = bookshop_book.set_dict()
        return books
    def clean_tag_results(self, tag_result: list, *args: str):
        """
        Pass a list and the value you want to remove from the list
        
        tag_result = ["'A Light in the ...', 'Tipping the Velvet', 'Soumission', 'Sharp Objects', 'Sapiens: A Brief History ..."]
        value = "..."
        """
        clean_result = []
        for value in args:
            # couldn't quite get the below code to work - decided to just clean the results by putting them through a for loop
            # clean_result = list(map(lambda x: x.replace(value, ""), tag_result))
            for result in tag_result:
                if value in result:
                    clean_result.append(result.replace(value, ""))

        return list(filter(None, clean_result))


website = Website("https://books.toscrape.com").connect()


bookshop = BookshopWebsiteScraper(website)

price_of_book = bookshop.get_tag("p")
name_of_book = bookshop.get_tag("h3")
clean_price_result = bookshop.clean_tag_results(price_of_book, "Â", "In stock")
test = bookshop.set_books(clean_price_result, name_of_book)


