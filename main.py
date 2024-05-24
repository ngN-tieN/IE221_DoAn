from Controllers.CardController import CardController
from DatabaseService import ConnectionService
from Controllers.StackController import StackController
from Controllers.StudySessionController import StudySessionController


def init(): #Tạo table nếu chưa có
    connection = ConnectionService.MySQLConnection()
    connection.init_stack_table()
    connection.init_card_table()
    connection.init_study_session_table()

if __name__ == "__main__": #Này để test back end
    init()
    StackController.add_stack("spain")
    # StackController.update_stack(2, "Japanese")
    stack_list = StackController.get_stacks()

    for stack in stack_list:
        print(stack)
    # print(StackController.get_stack_id_by_name('japanese'))
    # CardController.add_card('japanese', 'ohayo', 'good mornin')
    # CardController.delete_card(1)
    # CardController.update_card(2, '', "")
    # card_list = CardController.get_cards_by_stack_name('japanese')
    #
    # for card in card_list:
    #     print(card)
    # StudySessionController.add_session('japanese', 1)
    # StudySessionController.add_session('japanese', 3)
    # StudySessionController.add_session('japanese', 4)
    # session_list = StudySessionController.get_sessions_by_stack_name('japanese')
    # print(StudySessionController.get_average_score_week('japanese'))
    # print(StudySessionController.get_count_session_week('japanese'))
    # for session in session_list:
    #     print(session)
