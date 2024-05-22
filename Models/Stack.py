class Stack:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
    def __str__(self):
        return str([self.id, self.name])