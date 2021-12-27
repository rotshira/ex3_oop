import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        g = DiGraph()
        g_algo = GraphAlgo(g)
        self.assertEqual(g_algo.get_graph(),g)

    def test_load_from_json(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/T0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        self.assertEqual(g_algo.get_graph(), t)

    def test_save_to_json(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/T0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        g_algo.save_to_json(file + '_saved')
        self.assertEqual(g_algo.get_graph(),t)

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        file = 'C:/Users/shira/PycharmProjects/ex3_oop/src/data/A5.json'
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
        g_algo = GraphAlgo()
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/A3.json"
        g_algo.load_from_json(file)
        result, answer = (
        [0, 21, 22, 23, 24, 25, 26, 8, 7, 44, 43, 42, 41, 40, 39, 17, 14, 15, 38, 37, 36, 35, 34, 33, 32, 2, 3, 31, 30,
         13, 12, 11, 20, 19, 18, 10, 9, 1, 16, 6, 5, 28, 4, 29, 48, 47, 46, 45, 27], 8459.737919535499)

        self.assertEqual(g_algo.TSP(g_algo.nodes), (result, answer))


    def test_isconnected(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/A0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        self.assertEqual(g_algo.is_connected(),True)

    def test_centerPoint(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/A0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        t = g_algo.get_graph()
        self.assertEqual(g_algo.centerPoint(),(7, 6.806805834715163))

    def test_dijkstra(self):
        g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/A0.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        tes,res = g_algo.dijkstra(0)
        self.assertEqual(g_algo.dijkstra(0),(tes,res))
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/A5.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        tes,res = g_algo.dijkstra(0)
        self.assertEqual(g_algo.dijkstra(0),(tes,res))
        file = "C:/Users/shira/PycharmProjects/ex3_oop/src/data/A3.json"
        g_algo.load_from_json(file)  # init a GraphAlgo from a json file
        tes,res = g_algo.dijkstra(0)
        self.assertEqual(g_algo.dijkstra(0),(tes,res))
