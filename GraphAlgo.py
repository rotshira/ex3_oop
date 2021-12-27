import json
import os
import sys
from typing import List
from abc import ABCMeta
from src.Node import Node
import numpy as np
from src import DiGraph
# DiGraph.DiGraph()
from GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
import matplotlib.pyplot as plt




INF = sys.maxsize
root_path = os.path.dirname(os.path.abspath(__file__))


class GraphAlgo(GraphAlgoInterface, metaclass=ABCMeta):

    def __init__(self, graph :DiGraph = {}):
        self.graph = graph


    def _init_(self) -> None:
        self.vertex = {}
        self.edges = {}
        self.graph = DiGraph()


    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = DiGraph()
            with open(file_name, "r") as f:
                dict = json.load(f)
            for n in range(len(dict["Nodes"])):
                id = dict["Nodes"][n]["id"]
                if (len(dict["Nodes"][n]) == 1):
                    tuple = [np.random.uniform(35, 36), np.random.uniform(32, 33)]
                    graph.add_node(id, tuple)
                else:
                    pos = dict["Nodes"][n]["pos"]
                    tuple = pos.split(',')
                    graph.add_node(id, tuple)
            for e in range(len(dict["Edges"])):
                src = dict["Edges"][e]["src"]
                dest = dict["Edges"][e]["dest"]
                w = dict["Edges"][e]["w"]
                graph.add_edge(src, dest, w)
            self.edges = graph.edges
            self.nodes = graph.vertex
            self.graph = graph

            return True
        except Exception:
            return False

    def save_to_json(self, file_name: str) -> bool:
        list = []
        dict = {'Nodes': {(i): self.graph.vertex[i] for i in self.graph.vertex}}
        list.append(dict)
        dict1 = {'Edges': ''}
        list.append(dict1)
        for i in self.graph.vertex:
            for j in self.graph.all_out_edges_of_node(i):
                edge = {'src': i, 'dest': j, 'weight': self.graph.edges[(i, j)]}
                list.append(edge)
        out_file = open(file_name, "w")
        json.dump(list, out_file, indent=2)
        out_file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        shortest = []
        dist, path = self.dijkstra(id1)
        if id1 == -1 or id2 == -1:
            return float('inf'), []
        i = id2
        if dist[id2] != INF:
            shortest.append(id2)
            while i != id1:
                shortest.append(path[i])
                i = path[i]
            shortest.reverse()
        if dist[id2] == INF:
            dist[id2] = float('inf')
        return dist[id2], shortest

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if not self.is_connected():
            return [], 0.0
        copy_cities = [j for j in node_lst]  # copy node list
        result = []
        answer = 0
        # temp = node_lst[0].get_id()
        temp = 0
        result.append(copy_cities[0])
        copy_cities.remove(copy_cities[0])
        while len(copy_cities) >= 1:
            min = float('inf')
            same = -1
            place = -1
            for i in range(len(copy_cities)):
                open = copy_cities[i]
                dist = (self.shortest_path(temp, open))[0]
                if dist < min:
                    min = dist
                    same = open
                    place = i
            list = self.shortest_path(temp, same)[1]
            while len(list) >= 1:
                if list[0] not in result:
                    result.append(list[0])
                list.remove(list[0])
            q = copy_cities[place]
            temp = q
            copy_cities.remove(copy_cities[place])
            if len(copy_cities) == 1 and same + 1 not in result:
                result.append(same + 1)
            for i in self.graph.edges.values():
                answer = answer + i["w"]

        return result, answer




    def centerPoint(self) -> (int, float):
        if not self.is_connected():
            return None, None
        list = []
        max = 0
        for i in range(len(self.graph.vertex)):
            dist = self.dijkstra(i)[0]
            for i in dist:
                if dist[i] > max:
                    max = dist[i]
            list.append(max)
            max = 0
        min = INF
        node = -1
        for i in range(len(list)):
            if min > list[i]:
                min = list[i]
                node = i
        return node, min

    def is_connected(self):
        return float('inf') not in self.dijkstra(0)[0]

    # def plot_graph(self) -> None:
    #     for node in self.graph.vertex.values():
    #         # plot Nodes:
    #         node: Node
    #         loc = node.get_pos()
    #         if loc == None:
    #             node.set_location_random()  # placed in a uniform random
    #             x, y = node.get_location()
    #         else:
    #             x, y = loc[0], loc[1]
    #         plt.plot(x, y, markersize=4, marker='o', color='deepskyblue')
    #         plt.text(x, y, str(node.get_id()), color="navy", fontsize=9)
    #         for neibr_id, w in self._graph.getNeighboursDict(node.get_id()).items():
    #             # plot Edges:
    #             neibr = self._graph.getNode(neibr_id)
    #             loc_neibr = neibr.get_location()
    #             if loc_neibr == None:
    #                 neibr.set_location_random()  # placed in a uniform random
    #                 x_, y_ = neibr.get_location()
    #             else:
    #                 x_, y_ = loc_neibr[0], loc_neibr[1]
    #             plt.annotate("", xy=(x, y), xytext=(x_, y_), arrowprops=dict(arrowstyle="<-"), color="tomato", )
    #     plt.show()

    def dijkstra(self, start_node) -> (list, list):
        unvisited_nodes = list(self.graph.get_all_v())
        dist = {}
        # We'll use this dict to save the shortest known path to a node found so far
        path = {}
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        for node in unvisited_nodes:
            dist[node] = float('inf')
        # However, we initialize the starting node's value with 0
        dist[start_node] = 0
        # The algorithm executes until we visit all nodes
        while unvisited_nodes:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif dist[node] < dist[current_min_node]:
                    current_min_node = node
            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = self.graph.all_out_edges_of_node(current_min_node)
            for neighbor in neighbors:
                tentative_value = dist[current_min_node] + self.graph.edges[current_min_node, neighbor]
                if tentative_value < dist[neighbor]:
                    dist[neighbor] = tentative_value
                    # We also update the best path to the current node
                    path[neighbor] = current_min_node
            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
        return dist, path





