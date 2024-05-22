class CardDTO:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.front = kwargs.get('front')
        self.back = kwargs.get('back')
    def __str__(self):
        return str([self.id, self.front, self.back])