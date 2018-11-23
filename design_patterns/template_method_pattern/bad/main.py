from design_patterns.template_method_pattern.bad.sub import TurkeySub, VeggieSub


def main():
    turkey_sub = TurkeySub()
    turkey_sub.make()
    print('--------------------------')
    veggie_sub = VeggieSub()
    veggie_sub.make()


if __name__ == '__main__':
    main()
