from DatabaseService.AbstractDBService import AbstractDBService
from Models.Stack import Stack


class StackService(AbstractDBService):
    def __init__(self):
        super().__init__()

    def get_stacks(self):
        my_cursor = self._mydb.cursor()
        my_cursor.execute("SELECT * FROM STACK")
        my_result = my_cursor.fetchall()
        stack_list = []
        for result in my_result:
            stack = Stack(id=result[0], name=result[1])
            stack_list.append(stack)
        my_cursor.close()
        return stack_list

    def add_stack(self, stack_name):
        my_cursor = self._mydb.cursor()
        sql = "INSERT INTO STACK (name) VALUES (\"{}\")".format(stack_name)
        my_cursor.execute(sql)
        self._mydb.commit()
        self._mydb.close()

    def is_exists(self, stack_name):
        my_cursor = self._mydb.cursor()
        sql = "SELECT * FROM STACK WHERE name = \"{}\"".format(stack_name)
        my_cursor.execute(sql)
        if my_cursor.fetchone() is None:
            my_cursor.close()
            self._mydb.close()
            return False
        my_cursor.close()
        return True

    def delete_stack(self, stack_id):
        my_cursor = self._mydb.cursor()
        sql = "DELETE FROM STACK WHERE id = {}".format(stack_id)
        my_cursor.execute(sql)
        self._mydb.commit()
        row_count = my_cursor.rowcount
        my_cursor.close()
        return row_count

    def update_stack(self, stack_id, name):
        my_cursor = self._mydb.cursor()
        sql = """UPDATE STACK SET
                name = "{}" 
                WHERE id = {}""".format(name, stack_id)
        my_cursor.execute(sql)
        self._mydb.commit()
        row_count = my_cursor.rowcount
        my_cursor.close()
        return row_count

    def get_stack_id_by_name(self, stack_name):
        my_cursor = self._mydb.cursor()
        sql = "SELECT id FROM STACK WHERE name = \"{}\"".format(stack_name)
        my_cursor.execute(sql)
        stack_id = my_cursor.fetchone()[0]
        my_cursor.close()
        return stack_id
