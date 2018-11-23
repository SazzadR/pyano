from design_patterns.adapters_pattern.bad.ebooks import Kindle
from design_patterns.adapters_pattern.bad.person import Person
from design_patterns.adapters_pattern.bad.books import PaperBook


def main():
    person = Person()
    paper_book = PaperBook()
    person.read(paper_book)

    person = Person()
    kindle = Kindle()
    person.ebook_read(kindle)


if __name__ == '__main__':
    main()
