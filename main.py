from Controllers.CardController import CardController
from DatabaseService import ConnectionService
from Controllers.StackController import StackController


def init(): #Tạo table nếu chưa có
    connection = ConnectionService.MySQLConnection()
    connection.init_stack_table()
    connection.init_card_table()


if __name__ == "__main__": #Này để test back end
    init()
    # StackController.add_stack("spain")
    # StackController.update_stack(2, "Japanese")
    # stack_list = StackController.get_stacks()
    #
    # for stack in stack_list:
    #     print(stack)
    # print(StackController.get_stack_id_by_name('japanese'))
    # CardController.add_card('japanese', 'ohayo', 'good mornin')
    # CardController.delete_card(1)
    CardController.update_card(2, '', "")
    card_list = CardController.get_cards_by_stack_name('japanese')

    for card in card_list:
        print(card)