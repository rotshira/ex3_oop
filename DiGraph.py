from GraphInterface import GraphInterface
from Edge import Edge
from Node import Node




class DiGraph(GraphInterface):

    def __init__(self, vertex: dict = {}, edges: dict = {}):
        self.edges: dict = edges
        self.vertex: dict = vertex
        self.mc = 0

    def init(self, vertex: dict = {}, edges: dict = {}):
        self.edges = {}
        self.vertex = {}
        self.mc = 0


    def v_size(self) -> int:
        return len(self.vertex)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        d = {}
        for i in self.vertex:
            d1 = {i: self.all_out_edges_of_node(i)}
            d2 = {i: self.all_in_edges_of_node(i)}
            d.update(d1)
            d.update(d2)
        return d

    def all_in_edges_of_node(self, id1: int) -> dict:
        all_in_nodes = {}
        for n in self.vertex:
            p = (n, id1)
            if self.edges.get(p) is not None:
                d3 = {n: self.edges.get(p)}
                all_in_nodes.update(d3)
        return all_in_nodes

    def all_out_edges_of_node(self, id1: int) -> dict:
        all_out_edges = {}
        for n in self.vertex:
            p = (id1, n)
            if self.edges.get(p) is not None:
                d2 = {n: self.edges.get(p)}
                all_out_edges.update(d2)
        return all_out_edges

    def get_mc(self) -> int:
        return self.mc

    def add_node(self, node_id: int, pos: tuple = (0,0)) -> bool:
        if node_id in self.vertex:
            return False
        d = {node_id: pos}
        self.mc += 1
        self.vertex.update(d)
        return True

    def add_edge(self, id1: int, id2: int, weight: float = -1) -> bool:
        p = (id1, id2)
        d = {p: weight}
        # if d in self.edges:
        #     return False
        self.edges.update(d)
        self.mc += 1
        return True

    def __str__(self) -> str:
        return f"Graph: |V|: {self.v_size()}  ,|E|: {self.e_size()}"

    def remove_node(self, node_id: int) -> bool:
        if self.vertex.get(node_id) is None:
            return False
        for i in self.vertex:
            if self.edges.get((node_id, i)) is not None:
                del self.edges[(node_id, i)]
        del self.vertex[node_id]
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        p = (node_id1, node_id2)
        for key in self.edges:
            if key == p:
                del self.edges[key]
                break
        self.mc += 1
        return True

    def get_node(self, key: int):
        return self.vertex.get(key)

    def get_edge(self, src: int, dest: int):
        key = (src, dest)
        return self.edges.get(key)