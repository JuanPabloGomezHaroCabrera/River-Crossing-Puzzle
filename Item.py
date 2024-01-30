class Item:
    def __init__(self, name, id='_', eat=''):
        self.name = name
        self.id = id
        self.eat = eat
    
    def __str__(self):
        return self.id