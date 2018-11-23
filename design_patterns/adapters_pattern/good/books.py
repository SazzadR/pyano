from design_patterns.adapters_pattern.good.book_interface import BookInterface


class PaperBook(BookInterface):
    def open(self):
        print('opening the Paper Book.')

    def turn_page(self):
        print('turning the page of the Paper Book.')
