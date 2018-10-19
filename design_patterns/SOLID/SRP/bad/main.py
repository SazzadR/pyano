from core.database import MySQL
from datetime import datetime, timedelta


class SalesReporter:
    def between(self, from_date, to_date):
        # Get sales from DB
        sales = self.query_db_for_sales_between(from_date, to_date)

        # Return result
        return self.format(sales)

    def query_db_for_sales_between(self, from_date, to_date):
        mysql = MySQL()
        mysql.run("SELECT SUM(charge) FROM sales WHERE created_at BETWEEN '{}' AND '{}'".format(from_date, to_date))
        return int(mysql.cursor.fetchone()[0])

    def format(self, sales):
        return 'Sales: {}'.format(sales)


def main():
    sales_reporter = SalesReporter()
    from_date = datetime.today() - timedelta(15)
    to_date = datetime.today()

    print(sales_reporter.between(from_date, to_date))


if __name__ == '__main__':
    main()
