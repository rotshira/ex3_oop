class Node:
    def __init__(self, id: int = 0, pos: tuple = (), wieght: float = 0):
        self.id = id
        self.pos = pos
        self.weight = wieght

    def get_id(self):
        return self.id

    # setter method
    def set_id(self, x: int):
        self.id = x

    def get_pos(self):
        return self.pos

    # setter method
    def set_pos(self, x: tuple):
        self.pos = x



