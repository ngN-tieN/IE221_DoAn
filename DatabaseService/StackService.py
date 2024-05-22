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
        return stack_list

    def add_stack(self, stack_name):
        my_cursor = self._mydb.cursor()
        sql = "INSERT INTO STACK (name) VALUES (\"{}\")".format(stack_name)
        my_cursor.execute(sql)
        self._mydb.commit()

    def is_exists(self, stack_name):
        my_cursor = self._mydb.cursor()
        sql = "SELECT * FROM STACK WHERE name = \"{}\"".format(stack_name)
        my_cursor.execute(sql)
        if my_cursor.fetchone() is None:
            return False
        return True

    def delete_stack(self, stack_id):
        my_cursor = self._mydb.cursor()
        sql = "DELETE FROM STACK WHERE id = {}".format(stack_id)
        my_cursor.execute(sql)
        self._mydb.commit()
        return my_cursor.rowcount

    def update_stack(self, stack_id, name):
        my_cursor = self._mydb.cursor()
        sql = """UPDATE STACK SET
                name = "{}" 
                WHERE id = {}""".format(name, stack_id)
        my_cursor.execute(sql)
        self._mydb.commit()
        return my_cursor.rowcount

    def get_stack_id_by_name(self, stack_name):
        my_cursor = self._mydb.cursor()
        sql = "SELECT id FROM STACK WHERE name = \"{}\"".format(stack_name)
        my_cursor.execute(sql)
        return my_cursor.fetchone()[0]
