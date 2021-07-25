from unittest.case import TestCase
from books import ChildrenBook, HorrorBook
import unittest

class Test_ChildrenBook(unittest.TestCase):

    def setUp(self) -> None:
        self.children_book = ChildrenBook("Little Red Riding Hood", "Unknown")
        self.horror_book = HorrorBook("Goosebumps", "R. L. Stine")
    
    def test_to_dict(self):
        self.assertIn("title", self.children_book.to_dict(), f"title in {self.children_book}")
        self.assertIn("author", self.horror_book.to_dict())






if __name__ == "__main__":
    unittest.main()