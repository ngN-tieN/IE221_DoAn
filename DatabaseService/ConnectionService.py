import mysql.connector
import config


class MySQLConnection:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=config.mysql['host'],
            user=config.mysql['user'],
            password=config.mysql['passwd'],
            database=config.mysql['database'])

    def init_stack_table(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("""CREATE TABLE IF NOT EXISTS STACK
                            (id INT AUTO_INCREMENT PRIMARY KEY,
                              name TEXT NOT NULL""")

    def init_card_table(self):
        mycursor = self.mydb.cursor()
        mycursor.execute('CREATE TABLE IF NOT EXISTS CARD ' +
                         '(id INT AUTO_INCREMENT PRIMARY KEY,' +
                         'front TEXT NOT NULL,' +
                         'back TEXT NOT NULL,' +
                         'stack_id INT,' +
                         'FOREIGN KEY (id) ' +
                         'REFERENCES STACK (id) ' +
                         'ON DELETE CASCADE ')
