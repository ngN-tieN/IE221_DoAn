from DatabaseService.StudySessionService import StudySessionService
from Controllers.StackController import StackController


class StudySessionController():
    @staticmethod
    def add_session(stack_name, score):  # Thêm session với tham số là score, stack_id
        db_service = StudySessionService()
        name = stack_name.strip().lower()
        stack_id = StackController.get_stack_id_by_name(name)
        db_service.add_session(stack_id, score)

    @staticmethod
    def get_sessions_by_stack_name(stack_name):  #Trả về list StudySession theo stack_name
        db_service = StudySessionService()
        name = stack_name.strip().lower()
        stack_id = StackController.get_stack_id_by_name(name)
        return db_service.get_sessions_by_stack_id(stack_id)

    @staticmethod  #Trả về dict dang {'Thứ trong tuần': float} vd:{'MONDAY': 0.0,
                                                                # 'TUESDAY': 0.0,
                                                                # 'WEDNESDAY': 0.67,
                                                                #  'THURSDAY': 2.0, 'FRIDAY': 0.0, 'SATURDAY': 0.0, 'SUNDAY': 0.0}
    def get_average_score_week(stack_name):
        db_service = StudySessionService()
        name = stack_name.strip().lower()
        stack_id = StackController.get_stack_id_by_name(name)
        return db_service.get_average_score_week(stack_id)

    @staticmethod #Trả về dict như trên nhưng dạng  {'Thứ trong tuần': int}
    def get_count_session_week(stack_name):
        db_service = StudySessionService()
        name = stack_name.strip().lower()
        stack_id = StackController.get_stack_id_by_name(name)
        return db_service.get_count_session_week(stack_id)
