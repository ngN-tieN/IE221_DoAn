from Controllers.StackController import StackController
from DatabaseService.CardService import CardService


class CardController:
    @staticmethod
    def add_card(stack_name, front, back):  # Thêm card bằng tên stack
        db_service = CardService()
        name = stack_name.strip().lower()
        front = front.strip()
        back = back.strip()
        stack_id = StackController.get_stack_id_by_name(name)
        db_service.add_card(stack_id, front, back)

    @staticmethod
    def update_card(card_id,
                     front, back):  # Cập nhật card theo id (truyền ID với Front, Back cần cập nhật vào), trả về False nếu tên tồn tại
        # (trùng với tên hiện tại cũng False), ngược lại trả về True
        db_service = CardService()
        card = db_service.get_card(card_id)
        if front == "":
            front = card.front
        if back == "":
            back = card.back
        if db_service.update_card(card_id, front, back) == 0:
            return False
        print("Record is updated")
        return True

    @staticmethod
    def delete_card(card_id):  # Xóa card theo id
        db_service = CardService()
        if db_service.delete_card(card_id) == 0:
            print("Record id does not exist")
            return
        print("Record is deleted")

    @staticmethod
    def get_cards_by_stack_name(stack_name):  # Trả về tất cả card theo stack name [CardDTO, CardDTO]
        stack_id = StackController.get_stack_id_by_name(stack_name)
        db_service = CardService()
        return db_service.get_cards_by_stack_id(stack_id)

