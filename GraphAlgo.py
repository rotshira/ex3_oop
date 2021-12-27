
import json
import os
from typing import List
from numpy import double
import gui
from src.gui import gui
from DiGraph import DiGraph
import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface

INF = float('inf')
root_path = os.path.dirname(os.path.abspath(__file__))



class GraphAlgo(GraphAlgoInterface):

    #a constructor for algograph
    def __init__(self, graph: DiGraph = {}):
        self.graph: DiGraph = graph

#get the graph of graphalgo
    def get_graph(self) -> GraphInterface:
        return self.graph

    #load the graph from json file
    def load_from_json(self, file_name: str) -> bool:
        with open( file_name, 'r') as file:
            g = json.load(file)
        if g is None:
            return False
        graph = DiGraph()
        for n in g["Nodes"]:
            if 'pos' not in n:
                graph.add_node(node_id=n["id"], pos=(0, 0))
            else:
                sp = str(n['pos']).split(',')
                graph.add_node(node_id=int(n["id"]), pos=(float(sp[0]), float(sp[1])))
        for v in g["Edges"]:
            graph.add_edge(id1=v['src'], id2=v['dest'], weight=v['w'])
        self.__init__(graph)
        return True

    #save the graph to json file
    def save_to_json(self, file_name: str) -> bool:
        list = []
        dict = {'Nodes': {(i): self.graph.vertex[i] for i in self.graph.vertex}}
        list.append(dict)
        dict1 = {'Edges': ''}
        list.append(dict1)
        for i in self.graph.vertex:
            for j in self.graph.all_out_edges_of_node(i)[0]:
                edge = {'src': i, 'dest': j, 'weight': self.graph.edges[(i, j)]}
                list.append(edge)
        out_file = open(file_name, "w")
        json.dump(list, out_file, indent=2)
        out_file.close()
        if out_file is None:
            return False
        return True

    #calculate the distance between two points in the graph
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
            copy = [j for j in node_lst]
            pat = []
            answer = 0
            tmp = node_lst[0]
            pat.append(copy[0])
            copy.remove(copy[0])
            while len(copy) >= 1:
                minimum = double('inf')
                l = -1
                pos = -1
                for i in range(len(copy)):
                    open = copy[i]
                    dist = (self.shortest_path( tmp, open))[0]
                    if dist < minimum:
                        minimum = dist
                        l = open
                        pos = i
                list = self.shortest_path( tmp, l)[1]
                while len(list) >= 1:
                    if list[0] not in pat:
                        pat.append(list[0])
                    list.remove(list[0])
                q = copy[pos]
                tmp = q
                copy.remove(copy[pos])
                if len(copy) == 1 and l + 1 not in pat:
                    pat.append(l + 1)
                for i in self.graph.edges:
                    answer = answer + self.graph.edges.get(i)
            return pat, answer

   #check if the graph isconneceted or not
    def is_connected(self):
        return INF not in self.dijkstra(0)[0]

    #calc the center of sum graph
    def centerPoint(self) -> (int, float):
        if not self.is_connected():
            return None, None
        list = []
        for i in self.graph.vertex:
            dist = self.dijkstra(i)[0]  # list of distances
            # find maximum
            max = 0
            for j in range(len(dist)):
                if dist[j] > max:
                    max = dist[j]
            list.insert(i, max)
            max = 0
        min = float('inf')

        for i in range(len(list)):
            if min > list[i]:
                min = list[i]
                node = i
        return node, min

    #a function to calculate the shortestpath dist
    def shortest_path_help(self, id1: int, id2: int) -> (float):
        dist, path = self.dijkstra(id1)
        if id1 == -1 or id2 == -1:
            return float('inf')
        return dist[id2]

    # draw the graph in the screen
    def plot_graph(self) -> None:
        gui(self.get_graph())
        pass

    #a function of the algorithm of dijkstra
    def dijkstra(self, start_node):
        unvisited_nodes = list(self.graph.vertex)
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
        dist = {}
        # We'll use this dict to save the shortest known path to a node found so far
        path = {}
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        for node in unvisited_nodes:
            dist[node] = INF
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
            neighbors = self.graph.all_out_edges_of_node(current_min_node)[0]
            for neighbor in neighbors:
                tentative_value = dist[current_min_node] + self.graph.edges[(current_min_node, neighbor)]
                if tentative_value < dist[neighbor]:
                    dist[neighbor] = tentative_value
                    # We also update the best path to the current node
                    path[neighbor] = current_min_node
            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
        return dist, path

