import unittest
from abc import ABCMeta, abstractmethod


class EBookInterface(metaclass=ABCMeta):
    @abstractmethod
    def read(self): pass


class PDFBook(EBookInterface):
    def read(self):
        return 'reading a pdf book.'


class EpubBook(EBookInterface):
    def read(self):
        return 'reading a epub book.'


class EBookReader:
    def __init__(self, book: EBookInterface):
        self.book = book

    def read(self):
        return self.book.read()


class EBookReaderTest(unittest.TestCase):
    def test_it_can_read_a_pdf_book(self):
        book = PDFBook()
        reader = EBookReader(book)
        self.assertRegex(reader.read(), 'pdf book')

    def test_it_can_read_a_epub_book(self):
        book = EpubBook()
        reader = EBookReader(book)
        self.assertRegex(reader.read(), 'epub book')


if __name__ == '__main__':
    unittest.main()
