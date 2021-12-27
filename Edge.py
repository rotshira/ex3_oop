from Node import Node

class Edge:
    def __init__(self, src: int = Node, dest: int = Node, wieght : float = 0):
        self._src = src
        self._dest = dest
        self.weight = wieght

    def get_weight(self):
        return self.weight

    # setter method
    def set_weight(self, x: float):
        self.weight = x

    def get_src(self):
        return self._src

     # setter method
    def set_src(self, x : Node):
        self._src= x

    def get_dest(self):
        return self._dest

     # setter method
    def set_dest(self, x : Node):
        self._dest= x