from design_patterns.adapters_pattern.bad.book_interface import BookInterface
from design_patterns.adapters_pattern.bad.ebook_interface import EBookInterface


class Person:
    def read(self, book: BookInterface):
        book.open()
        book.turn_page()

    def ebook_read(self, ebook: EBookInterface):
        ebook.turn_on()
        ebook.press_next_button()
