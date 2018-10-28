from abc import ABCMeta, abstractmethod


class Receipt:
    def __init__(self, amount):
        self.amount = amount


class PaymentMethodInterface(metaclass=ABCMeta):
    @abstractmethod
    def accept_payment(self, receipt: Receipt): pass


class CashPayment(PaymentMethodInterface):
    def accept_payment(self, receipt: Receipt):
        print('Accepting ${} via cash.'.format(receipt.amount))


class CreditCardPayment(PaymentMethodInterface):
    def accept_payment(self, receipt: Receipt):
        print('Accepting ${} via credit card.'.format(receipt.amount))


class Checkout:
    def __init__(self, payment_method: PaymentMethodInterface):
        self.payment_method = payment_method

    def begain(self, receipt: Receipt):
        self.payment_method.accept_payment(receipt)


def main():
    transaction_1 = Checkout(CashPayment())
    transaction_1.begain(Receipt(100))

    transaction_2 = Checkout(CreditCardPayment())
    transaction_2.begain(Receipt(250))


if __name__ == '__main__':
    main()
