import mysql.connector


class MySQL:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='secret',
            database='pyano'
        )
        self.cursor = self.db.cursor()

    def run(self, query):
        self.cursor.execute(query)

# a = MySQL()
# a.cursor.execute('SELECT * FROM sales')
# print(a.cursor.fetchall())
