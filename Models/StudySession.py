class StudySession:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.score = kwargs.get('score')
        self.session_date = kwargs.get('session_date')
    def __str__(self):
        return str([self.id, self.score, self.session_date.strftime("%d/%m/%Y")])
