from LinkedList import LinkedList

class Vertex:
    def __init__(self, id, type, data=None):
        self.id = id
        self.data = data
        self.type = type
        self.edges = LinkedList()

    def __repr__(self):
        return f"Vertex({self.id}, {self.data})"