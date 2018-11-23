from design_patterns.adapters_pattern.good.book_interface import BookInterface
from design_patterns.adapters_pattern.good.ebook_interface import EBookInterface


class EBookAdapter(BookInterface):
    def __init__(self, ebook: EBookInterface):
        self.ebook = ebook

    def open(self):
        self.ebook.turn_on()

    def turn_page(self):
        self.ebook.press_next_button()
