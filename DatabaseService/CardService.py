from DatabaseService.AbstractDBService import AbstractDBService
from Models.Card import CardDTO


class CardService(AbstractDBService):
    def __init__(self):
        super().__init__()

    def get_cards_by_stack_id(self, stack_id):
        my_cursor = self._mydb.cursor()
        sql = "SELECT * FROM CARD WHERE stack_id = {}".format(stack_id)
        my_cursor.execute(sql)
        card_list = []
        for result in my_cursor.fetchall():
            card = CardDTO(id=result[0], front=result[1], back=result[2])
            card_list.append(card)
        return card_list

    def add_card(self, stack_id, front, back):
        my_cursor = self._mydb.cursor()
        sql = "INSERT INTO CARD (front, back, stack_id) VALUES (\"{}\", \"{}\", {})".format(front, back, stack_id)
        my_cursor.execute(sql)
        self._mydb.commit()

    def delete_card(self, card_id):
        my_cursor = self._mydb.cursor()
        sql = "DELETE FROM CARD WHERE id = {}".format(card_id)
        my_cursor.execute(sql)
        self._mydb.commit()
        return my_cursor.rowcount

    def update_card(self, card_id, front, back):
        my_cursor = self._mydb.cursor()
        sql = """UPDATE CARD SET
                        front = "{}",
                        back = "{}"  
                        WHERE id = {}""".format(front, back, card_id)
        my_cursor.execute(sql)
        self._mydb.commit()
        return my_cursor.rowcount

    def get_card(self, card_id):
        my_cursor = self._mydb.cursor()
        sql = "SELECT * FROM CARD WHERE id = {}".format(card_id)
        my_cursor.execute(sql)
        card = my_cursor.fetchone()
        return CardDTO(id=card[0], front=card[1], back=card[2])
