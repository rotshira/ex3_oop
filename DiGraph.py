from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    #a constructor for graph
    def __init__(self, vertex: dict = {}, edges: dict = {}):
        self.edges: dict = edges
        self.vertex: dict = vertex
        self.mc = 0

     #a function to return the size of  vertex of the graph
    def v_size(self) -> int:
        return len(self.vertex)

     #a function to return the size of  edges of the graph
    def e_size(self) -> int:
        return len(self.edges)

    # prints a dict with all the graph's vertices.
    def get_all_v(self) -> dict:
        d = {}
        for i in self.vertex:
            d1 = {i: f"{i}: |edges out|: {self.all_out_edges_of_node(i)[1]}  ,|edges in|: {self.all_in_edges_of_node(i)[1]}"}
            d.update(d1)
        return d

    # prints a dict with all the graph's vertices.(all in edges)
    def all_in_edges_of_node(self, id1: int) -> dict:
        all_in_nodes = {}
        for n in self.vertex:
            p = (n, id1)
            if self.edges.get(p) is not None:
                d3 = {n: self.edges.get(p)}
                all_in_nodes.update(d3)
        return all_in_nodes, len(all_in_nodes)


    # prints a dict with all the graph's vertices.(all out edges)
    def all_out_edges_of_node(self, id1: int) -> dict:
        all_out_edges = {}
        for n in self.vertex:
            p = (id1, n)
            if self.edges.get(p) is not None:
                d2 = {n: self.edges.get(p)}
                all_out_edges.update(d2)
        return all_out_edges,len(all_out_edges)

    #return how many function was done in the graph
    def get_mc(self) -> int:
        return self.mc

    #add node to the graph
    def add_node(self, node_id: int, pos: tuple = (0,0)) -> bool:
        if node_id in self.vertex:
            return False
        d = {node_id: pos}
        self.vertex.update(d)
        self.mc += 1
        return True

    #add edge to the graph
    def add_edge(self, id1: int, id2: int, weight: float =-1) -> bool:
        p = (id1, id2)
        d = {p: weight}
        # if d in self.edges:
        #     return False
        self.edges.update(d)
        self.mc += 1
        return True

    #overide the str function to show the amount of nodes and edges
    def __str__(self) -> str:
        return f"Graph: |V|: {self.v_size()}  ,|E|: {self.e_size()}"

    #remove node from the graph
    def remove_node(self, node_id: int) -> bool:
        if self.vertex.get(node_id) is None:
            return False
        for i in self.vertex:
            if self.edges.get((node_id, i)) is not None:
                del self.edges[(node_id, i)]
        del self.vertex[node_id]
        self.mc += 1
        return True

    #remove an edge from the graph
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        p = (node_id1, node_id2)
        for key in self.edges:
            if key == p:
                del self.edges[key]
                break
        self.mc += 1
        return True

    #get specific node from the graph
    def get_node(self, key: int):
        return self.vertex.get(key)

    #get specific edge from the graph
    def get_edge(self, src: int, dest: int):
        key = (src, dest)
        return self.edges.get(key)