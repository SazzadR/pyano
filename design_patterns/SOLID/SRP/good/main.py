import json
from core.database import MySQL
from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta


class SalesRepository:
    def between(self, from_date, to_date):
        mysql = MySQL()
        mysql.run("SELECT SUM(charge) FROM sales WHERE created_at BETWEEN '{}' AND '{}'".format(from_date, to_date))
        return int(mysql.cursor.fetchone()[0])


class FormatterInterface(metaclass=ABCMeta):
    @abstractmethod
    def format(self, sales): pass


class HtmlFormatter(FormatterInterface):
    def format(self, sales):
        return 'Sales: {}'.format(sales)


class JsonFormatter(FormatterInterface):
    def format(self, sales):
        response = {'sales': sales}
        return json.dumps(response)


class SalesReporter:
    def __init__(self, sales_repository: SalesRepository):
        self.sales_repository = sales_repository

    def between(self, from_date, to_date, formatter_interface: FormatterInterface):
        sales = self.sales_repository.between(from_date, to_date)

        return formatter_interface.format(sales)


def main():
    sales_reporter = SalesReporter(SalesRepository())
    from_date = datetime.today() - timedelta(15)
    to_date = datetime.today()

    print(sales_reporter.between(from_date, to_date, HtmlFormatter()))
    print(sales_reporter.between(from_date, to_date, JsonFormatter()))


if __name__ == '__main__':
    main()
