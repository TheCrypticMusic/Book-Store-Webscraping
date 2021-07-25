from unittest.case import TestCase
from books import BookshopWebiteBook
import unittest

class Test_ChildrenBook(unittest.TestCase):

    def setUp(self) -> None:
        self.children_book = BookshopWebiteBook(0, "Little Red Riding Hood", "£53.00")
        self.horror_book = BookshopWebiteBook(1, "Goosebumps", "£55.00")
    
    def test_to_dict(self):
        self.assertIn(0, self.children_book.set_dict())
        self.assertIn("Little Red Riding Hood", self.children_book.set_dict()[0]["title"])






if __name__ == "__main__":
    unittest.main()