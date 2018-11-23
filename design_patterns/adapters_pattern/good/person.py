from design_patterns.adapters_pattern.good.book_interface import BookInterface


class Person:
    def read(self, book: BookInterface):
        book.open()
        book.turn_page()
