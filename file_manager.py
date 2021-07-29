from abc import ABC, abstractmethod
import csv
from os import name
import sqlite3
from sqlite3.dbapi2 import Cursor, Error, OperationalError


class SaveFileManager(ABC):

    @staticmethod
    @abstractmethod
    def save(book):
        pass


class LoadFileManger(ABC):

    @abstractmethod
    def load(file):
        pass


class LoadCSVFile(LoadFileManger):

    @staticmethod
    def load(file):
        with open(file, "rt") as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                print(line)


class SaveToTxtFile(SaveFileManager):

    @staticmethod
    def save(book: dict):
        with open("books", "w") as f:
            for book_number, book_details in book.items():
                f.write(f"\n{str(book_number)} {book_details}")


class SaveToCSVFile(SaveFileManager):

    @staticmethod
    def save(book: dict):
        with open("books_csv.csv", "w", newline="") as f:
            csv_writer = csv.DictWriter(f, delimiter=",", quotechar='"', fieldnames=[
                                        "title", "author", "genre"])
            csv_writer.writerow(book)


class DatabaseManager(ABC):

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    @abstractmethod
    def connect_to_db(self, path_name_to_db):
        pass

    @abstractmethod
    def create_db(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def remove_table(self):
        pass

    @abstractmethod
    def show_table(self):
        pass

    @abstractmethod
    def insert_into_table(self, values):
        pass


class SQLite3DB(DatabaseManager):

    
    def create_db(self):
        """
        SQLite3 Database created based on name given during object instantiation 
        """
        self.conn = sqlite3.connect(f"{self.db_name}")
        print(f"SQLite DB Created: {self.db_name}")

    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect(
                f"file:{self.db_name}?mode=rw", uri=True)
            print(f"Connection made to {self.db_name}")
        except sqlite3.OperationalError as err:
            print(f"The error {err} occured.\nIf you wanted to create a new DB then use the following commands:\n\n"
                  "db = SQLite3DB(db_name)\ndb.create_db()\n\n")
        return self.conn

    
    def create_table(self):
        """
        This allows the user to create a table called books with the following fields:

        id INTEGER PRIMARY KEY, title VARCHAR(30), price FLOAT(5), qty SMALLINT location VARCHAR(20) 
        """
        try:
            cur = self.conn.cursor()
            cur.execute(f'''CREATE TABLE books (id INTEGER PRIMARY KEY, title VARCHAR(30), price FLOAT(5), qty SMALLINT, location VARCHAR(20))''')
            print(f"books created with the following fields: id, title, price, qty location")
        except OperationalError as err:
            print(f"An error as occurred: {err}")

    def remove_table(self):
        """Removes table named books from database"""
        cur = self.conn.cursor()
        cur.execute(f"DROP TABLE books")
        print(f"books removed from {self.db_name}")

    def show_table(self):
        """Shows tables present in DB
        """
        cur = self.conn.cursor()
        cur.execute('SELECT name from sqlite_master where type= "table"')
        print(cur.fetchall())

        
    def insert_into_table(self, values: tuple):
        """
        Add data into the table

        Args:
            values (tuple): insert 4 values into the database. (title of book, price of book, location)
        """
        cur = self.conn.cursor()
        cur.execute("INSERT INTO books (title, price, qty, location) VALUES (?, ?, ?, ?)", (values))
        self.conn.commit()



