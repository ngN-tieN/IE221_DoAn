from DatabaseService.AbstractDBService import AbstractDBService
from Models.StudySession import StudySession


class StudySessionService(AbstractDBService):
    def __init__(self):
        super().__init__()

    def add_session(self, stack_id, score):
        my_cursor = self._mydb.cursor()
        sql = "INSERT INTO STUDYSESSION (score, stack_id) VALUES ({}, {})".format(score, stack_id)
        my_cursor.execute(sql)
        self._mydb.commit()
        my_cursor.close()

    def get_sessions_by_stack_id(self, stack_id):
        my_cursor = self._mydb.cursor()
        sql = "SELECT * FROM STUDYSESSION WHERE stack_id={}".format(stack_id)
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        session_list = []
        for row in result:
            session = StudySession(id=row[0], score=row[1], session_date=row[2])
            session_list.append(session)
        my_cursor.close()
        return session_list

    def get_average_score_week(self, stack_id):
        my_cursor = self._mydb.cursor(dictionary=True)
        sql = """SELECT 
	                ROUND(AVG(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'MONDAY' THEN score ELSE score = 0 END), 2) AS MONDAY,
                    ROUND(AVG(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'TUESDAY' THEN score ELSE score = 0 END), 2) AS TUESDAY,
                    ROUND(AVG(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'WEDNESDAY' THEN score ELSE score = 0 END), 2) AS WEDNESDAY,
                    ROUND(AVG(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'THURSDAY' THEN score ELSE score = 0 END), 2) AS THURSDAY,
                    ROUND(AVG(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'FRIDAY' THEN score ELSE score = 0 END), 2) AS FRIDAY,
                    ROUND(AVG(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'SATURDAY' THEN score ELSE score = 0 END), 2) AS SATURDAY,
                    ROUND(AVG(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'SUNDAY' THEN score ELSE score = 0 END), 2) AS SUNDAY
                FROM flashcard.studysession
                WHERE week(session_date, 5) = week(now(),5)
                AND stack_id={}""".format(stack_id)
        my_cursor.execute(sql)
        result = my_cursor.fetchall()[0]
        my_cursor.close()

        for k, v in result.items():
            result[k] = float(v)
        return result

    def get_count_session_week(self, stack_id):
        my_cursor = self._mydb.cursor(dictionary=True)
        sql = """SELECT 
	                COUNT(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'MONDAY' THEN id END) AS MONDAY,
                    COUNT(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'TUESDAY' THEN id END) AS TUESDAY,
                    COUNT(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'WEDNESDAY' THEN id END) AS WEDNESDAY,
                    COUNT(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'THURSDAY' THEN id END) AS THURSDAY,
                    COUNT(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'FRIDAY' THEN id END) AS FRIDAY,
                    COUNT(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'SATURDAY' THEN id END) AS SATURDAY,
                    COUNT(CASE WHEN DAYNAME(CAST(studysession.session_date AS DATE)) = 'SUNDAY' THEN id END) AS SUNDAY
                FROM flashcard.studysession
                WHERE week(session_date,5) = week(now(),5)
                AND stack_id={};""".format(stack_id)
        my_cursor.execute(sql)
        result = my_cursor.fetchall()[0]
        my_cursor.close()
        return result
