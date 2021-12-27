import unittest

from DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.assertEqual(DiGraph.v_size(g), 4)
        self.assertNotEqual(DiGraph.v_size(g), 7)


    def test_e_size(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(DiGraph.e_size(g), 5)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.assertEqual(DiGraph.e_size(g), 5)
        self.assertNotEqual(DiGraph.e_size(g), 7)

    def test_get_all_v(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        d = {0: '0: |edges out|: 1  ,|edges in|: 1', 1: '1: |edges out|: 3  ,|edges in|: 1', 2: '2: |edges out|: 1  ,|edges in|: 1', 3: '3: |edges out|: 0  ,|edges in|: 2'}
        self.assertEqual(g.get_all_v(),d)

    def test_all_in_edges_of_node(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.assertEqual(g.all_in_edges_of_node(0), ({1: 1.1}, 1))
        self.assertEqual(g.all_in_edges_of_node(1), ({0: 1}, 1))

    def all_out_edges_of_node(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.assertEqual(g.all_out_edges_of_node(0),{(0,1):1})

    def test_get_mc(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.assertEqual(g.get_mc(),7)


    def test_add_node(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        self.assertEqual(g.get_node(0), (0, 0))
        self.assertEqual(g.get_node(1), (0, 0))
        self.assertEqual(g.get_node(2), (0, 0))
        self.assertEqual(g.get_node(3), (0, 0))

    def test_add_edge(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        self.assertEqual(g.get_edge(0,1) , 1)
        g.add_edge(1, 0, 1.1)
        self.assertEqual(g.get_edge(1,0) , 1.1)
        g.add_edge(1, 2, 1.3)
        self.assertEqual(g.get_edge(1,2) , 1.3)
        g.add_edge(2, 3, 1.1)
        self.assertEqual(g.get_edge(2,3) , 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(g.get_edge(1,3) , 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.assertEqual(g.get_edge(1,3) , 10)

    def test_remove_node(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(2)
        g.remove_node(3)
        self.assertEqual(g.get_node(0),None)
        self.assertEqual(g.get_node(1),None)
        self.assertEqual(g.get_node(2),None)
        self.assertEqual(g.get_node(3),None)

    def test_remove_edge(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.remove_edge(1,0)
        g.remove_edge(1,2)
        g.remove_edge(2,3)
        g.remove_edge(1,3)
        self.assertEqual(g.get_edge(1,3),None)
        self.assertEqual(g.get_edge(1,0),None)
        self.assertEqual(g.get_edge(1,2),None)
        self.assertEqual(g.get_edge(2,3),None)
        self.assertEqual(g.get_edge(1,3),None)

    def test_get_node(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(2)
        g.remove_node(3)
        self.assertEqual(g.get_node(0),None)
        self.assertEqual(g.get_node(1),None)
        self.assertEqual(g.get_node(2),None)
        self.assertEqual(g.get_node(3),None)

    def test_get_edge(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.remove_edge(1,0)
        g.remove_edge(1,2)
        g.remove_edge(2,3)
        g.remove_edge(1,3)
        self.assertEqual(g.get_edge(1,3),None)
        self.assertEqual(g.get_edge(1,0),None)
        self.assertEqual(g.get_edge(1,2),None)
        self.assertEqual(g.get_edge(2,3),None)
        self.assertEqual(g.get_edge(1,3),None)

if __name__ == '__main__':
    TestDiGraph()
