class Card:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.front = kwargs.get('front')
        self.back = kwargs.get('back')
        self.stack_id = kwargs.get('stack_id')