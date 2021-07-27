from abc import ABC, abstractmethod
import csv
import sqlite3
from sqlite3.dbapi2 import Cursor, Error

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
            csv_writer = csv.DictWriter(f, delimiter=",", quotechar='"', fieldnames=["title", "author", "genre"])
            csv_writer.writerow(book)

class DatabaseManager(ABC):

    @abstractmethod
    def connect_to_db(self, path_name_to_server):
        pass

    @abstractmethod
    def db_query(self, query):
        pass

class SQLite3DB(DatabaseManager):

    def connect_to_db(self, path_name_to_server):
        connection = None
        try:
            connection = sqlite3.connect(path_name_to_server)
            print(f"Connection made to {path_name_to_server}")
        except Error as e:
            print(f"The error {e} occured")
        
        return connection



