from abc import abstractmethod
import csv

class FileManager:

    @staticmethod
    @abstractmethod
    def to_file(book):
        pass

class TxtFile(FileManager):

    @staticmethod
    def to_file(book: str):
        with open("books", "a") as f:
            f.write(book)

class CSVFile(FileManager):

    @staticmethod
    def to_file(book: dict):
        with open("books_csv.csv", "a", newline="") as f:
            csv_writer = csv.DictWriter(f, delimiter=",", quotechar='"', fieldnames=["title", "author", "genre"])
            csv_writer.writerow(book)
