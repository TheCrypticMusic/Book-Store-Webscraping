
from abc import abstractmethod
from file_manager import SQLite3DB
from books import BookshopWebiteBook  
import requests
from bs4 import BeautifulSoup

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

class WebsiteScraper:

    def __init__(self, html_response):
        self.html_response = html_response
        self.__get_html()

    def __get_html(self) -> str:
        self.soup = BeautifulSoup(self.html_response, "lxml")
        return self.soup

    def get_href_links(self, tag="href") -> list:
        """Grabs all href's on a page

        Args:
            tag (str, optional): Defaults to "href".

        Returns:
            list: href's in a list
        """
        href_list = []
        for a_tag in self.soup.find_all("a", href=True):
            href_list.append(a_tag[tag].strip())
        return href_list

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

    def get_tag(self, tag: str) -> list:
        """searches through the html for the tag given"""
        tag_results = []
        for html in self.soup(tag):
            if html.text.strip() == "":
                continue
            tag_results.append(html.text.strip())
        return tag_results

    @abstractmethod
    def next_page(self):
        pass

class BookshopWebsiteScraper(WebsiteScraper):

    def set_books(self, title: str, price: str):
        """Sets books from the website into a dict

        Args:
            title (str): [description]
            price (str): [description]
        """
        for book_title, book_price in zip(price, title):
            bookshop_book = BookshopWebiteBook()
            bookshop_book.add_book(book_title, book_price)


    def next_page(self, page_number: int):
        """Can be used in conjuction with a loop where you increment numbers (page numbers)
        Exampe: 
            website = Website("https://books.toscrape.com").connect()

            for page_number in range(2, 5):
                book_test = BookshopWebsiteScraper(website)
                prices = book_test.get_tag("p")
                books = book_test.get_tag("h3")
                clean_prices = book_test.clean_tag_results(prices, "Â", "In stock")
                book_test.set_books(clean_prices, books)
                website = book_test.next_page(page_number)
        Args:
            page_number (int)

        Returns:
            [Request]
        """
        url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
        next_page_url = Website(url).connect()
        return next_page_url