from DatabaseService.AbstractDBService import AbstractDBService


class MySQLConnection(AbstractDBService):
    def __init__(self):
        AbstractDBService.__init__(self)

    def init_stack_table(self):
        my_cursor = self._mydb.cursor()
        my_cursor.execute("""CREATE TABLE IF NOT EXISTS STACK
                            (id INT AUTO_INCREMENT PRIMARY KEY,
                              name TEXT NOT NULL""" + ")")
        my_cursor.close()
    def init_card_table(self):
        my_cursor = self._mydb.cursor()
        my_cursor.execute('CREATE TABLE IF NOT EXISTS CARD ' +
                          '(id INT AUTO_INCREMENT PRIMARY KEY,' +
                          'front TEXT NOT NULL,' +
                          'back TEXT NOT NULL,' +
                          'stack_id INT,' +
                          'FOREIGN KEY (stack_id) ' +
                          'REFERENCES STACK (id) ' +
                          'ON DELETE CASCADE )')
        my_cursor.close()

    def init_study_session_table(self):
        my_cursor = self._mydb.cursor()
        my_cursor.execute('CREATE TABLE IF NOT EXISTS STUDYSESSION ' +
                          '(id INT AUTO_INCREMENT PRIMARY KEY,' +
                          'score INT NOT NULL,' +
                          'session_date DATETIME DEFAULT CURRENT_TIMESTAMP, ' +
                          'stack_id INT,' +
                          'FOREIGN KEY (stack_id) ' +
                          'REFERENCES STACK (id) ' +
                          'ON DELETE CASCADE )')
        my_cursor.close()