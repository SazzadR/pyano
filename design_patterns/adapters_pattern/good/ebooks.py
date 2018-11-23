from design_patterns.adapters_pattern.good.ebook_interface import EBookInterface


class Kindle(EBookInterface):
    def turn_on(self):
        print('turn the Kindle on.')

    def press_next_button(self):
        print('press the next button on the Kindle.')
