## ex3_oop 💻







# **Explanation of the assignment:**
# In Ex3 we was need to implement two methods ,the first is of graph with nodes(location and id) and with edges(src,dest,weight).the second method that we was need to implement is of algorithms to do on our graph.(TSP,Shortestpath,load&save).
_
_
_

# **UML**







![WhatsApp Image 2021-12-28 at 09 10 02](https://user-images.githubusercontent.com/93703549/147538679-1092f800-da54-484a-9eae-b80f915bdd39.jpeg)




















 # **Explanation of the use in the function  Graphalgo.py**

In graphalgo.py we got load method:
this method you need to enter your file name to use this function.

In graphalgo.py we got save method:
 this method you need to enter your file name that you want to save in this function.

In graphalgo.py we got shortest path method:
 this method you need to enter source(id) node and destination(id) node to find the shortest path using Dijkstra algorithm.

In graphalgo.py we got is connected method:
 this method you need to enter source (id) node using Dijkstra algorithm to check is the graph is connected.

In graphalgo.py we got TSP method:
 this method you need to enter list of nodes(list) in the graph and the algorithm find the path between them.
 
 In graphalgo.py we got center method:
In this method you need to return center of graph



# **Explanation of the use in the function DIGraph.py**

In graph.py we got size v method:
In this method return the size of the nodes in the graph.

In graph.py we got size e method:
In this method return the size of the edges in the graph.
In graph.py we got get_all_v() method:

In this method return a ‘dict’ with the size of all out_nodes and in_nodes for each vertex in the graph.
In graph.py we got all_out_egdes_from_node method:
In this method return a ‘dict’ with the out edges from node.

In graph.py we got all_in_egdes_from_node method:
In this method return a ‘dict’ with the in edges from node.

In graph.py we got add node() method:
In this method we add a ‘dict’ of node by id node from the user and location from the user.

In graph.py we got add edge() method:
In this method we add a ‘dict’ of edge by id src and id dest from the user and weight of edge from the user.

In graph.py we got remove node() method:
In this method we remove a ‘dict’ of node by id node from the user .
We also remove all the edges that are connected to the node.

In graph.py we got remove edge() method:
In this method we remove a ‘dict’ of edge by id src and id dest from the .

In graph.py we got get mc() method:
In this method we return mc in the graph (all the method that was made on some graph).


# **Tests**

The TestDiGraph and TestGraphAlgo classes run tests on both of the classes,respectively. We tested them using JSON files which hold great amounts of nodes and edges in order to check efficiency.

# **running times**









![WhatsApp Image 2021-12-27 at 21 02 47](https://user-images.githubusercontent.com/93703549/147511141-b9353477-ab7d-4f64-9f19-85ac6828a25f.jpeg)








# **Computer information**
Device name DESKTOP-2IQM7II Processor 11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz 2.30 GHz Installed RAM 16.0 GB (15.7 GB usable) Device ID 89BCF75A-3AEF-4F71-BF3A-766DC75AF34C Product ID 00330-54020-20314-AAOEM System type 64-bit operating system, x64-based processor Pen and touch No pen or touch input is available for this display







# Graph photographs

# check1-A0.json :








![WhatsApp Image 2021-12-28 at 11 47 42](https://user-images.githubusercontent.com/93703549/147553425-f575442d-d317-447a-9835-66b58b1f2afd.jpeg)














# check2-A5.json :







![WhatsApp Image 2021-12-28 at 11 23 12](https://user-images.githubusercontent.com/93703549/147551637-13c44c2a-af0b-49a1-a231-0adc0f8677b6.jpeg)


