import unittest


class PDFBook:
    def read(self):
        return 'reading a pdf book.'


class EBookReader:
    def __init__(self, book: PDFBook):
        self.book = book

    def read(self):
        return self.book.read()


class EBookReaderTest(unittest.TestCase):
    def test_it_can_read_a_pdf_book(self):
        book = PDFBook()
        reader = EBookReader(book)
        self.assertRegex(reader.read(), 'pdf book')


if __name__ == '__main__':
    unittest.main()
