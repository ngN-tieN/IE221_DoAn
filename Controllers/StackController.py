from DatabaseService.StackService import StackService


class StackController:

    @staticmethod
    def add_stack(stack_name):  #Thêm stack bằng tên, trả về False nếu tên tồn tại, ngược lại trả về True
        db_service = StackService()
        name = stack_name.strip().lower()
        if db_service.is_exists(name):
            return False
        db_service.add_stack(name)
        return True

    @staticmethod
    def update_stack(stack_id,
                     stack_name):  # Cập nhật stack theo id (truyền ID với Tên cần cập nhật vào), trả về False nếu tên tồn tại
        # (trùng với tên hiện tại cũng False), ngược lại trả về True
        db_service = StackService()
        name = stack_name.strip().lower()
        if stack_id == "":
            return False
        if db_service.is_exists(name):
            print("Name exists")
            return False
        if db_service.update_stack(stack_id, name) == 0:
            print("Record id does not exist")
            return False
        print("Record is updated")
        return True

    @staticmethod
    def delete_stack(stack_id):  #Xóa stack theo id
        db_service = StackService()
        if db_service.delete_stack(stack_id) == 0:
            print("Record id does not exist")
            return
        print("Record is deleted")

    @staticmethod
    def get_stacks():  #Trả về tất cả stack [Stack, Stack]
        db_service = StackService()
        return db_service.get_stacks()

    @staticmethod
    def get_stack_id_by_name(stack_name):  #Trả về stack id theo name
        db_service = StackService()
        name = stack_name.strip().lower()
        return db_service.get_stack_id_by_name(stack_name)