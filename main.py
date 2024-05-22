from DatabaseService import ConnectionService
from Controllers.StackController import StackController


def Init(): #Tạo table nếu chưa có
    connection = ConnectionService.MySQLConnection()
    connection.init_stack_table()
    connection.init_card_table()


if __name__ == "__main__": #Này để test back end
    Init()
    # StackController.add_stack("spain")
    StackController.update_stack(2, "Japanese")
    stack_list = StackController.get_stacks()
    for stack in stack_list:
        print(stack)
