from design_patterns.template_method_pattern.good.example_1.sub import TurkeySub, VeggieSub


def main():
    turkey_sub = TurkeySub()
    turkey_sub.make()
    print('--------------------------')
    veggie_sub = VeggieSub()
    veggie_sub.make()


if __name__ == '__main__':
    """
    The Template Method Pattern is a behavioral design pattern that defines the program skeleton of an algorithm 
    in an operation, deferring some steps to subclasses. It lets one redefine certain steps of an algorithm 
    without changing the algorithm's structure
    """
    main()
