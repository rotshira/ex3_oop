import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class gatest(unittest.TestCase):

    def test_get_graph(self):
        g = DiGraph()
        g_algo = GraphAlgo(g)
        self.assertEqual(g_algo.get_graph(),g)

    def test_load_from_json(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "\\data\\T0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        self.assertEqual(g_algo.get_graph(),t)

    def test_save_to_json(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "\\data\\T0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        g_algo.save_to_json(file + '_saved')
        self.assertEqual(g_algo.get_graph(),t)

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        file = '\\data\\A5.json'
        g_algo.load_from_json(file)
        g_algo.get_graph().remove_edge(13, 14)
        g_algo.save_to_json(file + "_edited")
        dist,path = g_algo.shortest_path(1, 7)
        self.assertEqual(g_algo.shortest_path(1,7),(dist,path))
        dist,path = g_algo.shortest_path(47, 19)
        self.assertEqual(g_algo.shortest_path(47,19),(dist,path))
        dist, path = g_algo.shortest_path(20, 2)
        self.assertEqual(g_algo.shortest_path(20,2),(dist,path))
        dist, path= g_algo.shortest_path(2, 20)
        self.assertEqual(g_algo.shortest_path(2,20),(dist,path))

    def test_TSP(self):
        pass

    def test_isconnected(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "\\data\\A0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        self.assertEqual(g_algo.is_connected(),True)

    def test_centerPoint(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "\\data\\A0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        self.assertEqual(g_algo.centerPoint(),(7, 6.806805834715163))

    def test_dijkstra(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "\\data\\A0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        tes,res = g_algo.dijkstra(0)
        self.assertEqual(g_algo.dijkstra(0),(tes,res))
        file = "\\data\\A5.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        tes,res = g_algo.dijkstra(0)
        self.assertEqual(g_algo.dijkstra(0),(tes,res))
        file = "\\data\\A3.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        tes,res = g_algo.dijkstra(0)
        self.assertEqual(g_algo.dijkstra(0),(tes,res))
