class Item:

    def __init__(self, id, name, status = "To Do"):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def fetchTrelloDetails(cls, card, list):
        return cls(card["id"], card["name"], list["name"])

    def initial(self):
        self.status = "To Do"
    
    def completed(self):
        self.status = "Done"

    def started(self):
        self.status = "In Progress"
    
