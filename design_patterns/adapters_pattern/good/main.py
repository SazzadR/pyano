from design_patterns.adapters_pattern.good.ebooks import Kindle
from design_patterns.adapters_pattern.good.person import Person
from design_patterns.adapters_pattern.good.books import PaperBook
from design_patterns.adapters_pattern.good.ebook_adapter import EBookAdapter


def main():
    person = Person()
    paper_book = PaperBook()
    person.read(paper_book)

    person = Person()
    kindle = Kindle()
    person.read(EBookAdapter(kindle))


if __name__ == '__main__':
    main()
