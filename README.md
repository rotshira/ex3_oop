# ex3_oop

Explanation of the assignment:
In Ex3 we was need to implement two methods ,the first is of graph with nodes(location and id) and with edges(src,dest,weight).the second method that we was need to implement is of algorithms to do on our graph.(TSP,Shortestpath,load&save).

2)Explanation of the use in the function
Graphalgo.py
In graphalgo.py we got load method:
In this method you need to enter your file name to use this function.

In graphalgo.py we got save method:
In this method you need to enter your file name that you want to save in this function.

In graphalgo.py we got shortest path method:
In this method you need to enter source(id) node and destination(id) node to find the shortest path using Dijkstra algorithm.

In graphalgo.py we got is connected method:
In this method you need to enter source (id) node using Dijkstra algorithm to check is the graph is connected.

In graphalgo.py we got TSP method:
In this method you need to enter list of nodes(list) in the graph and the algorithm find the path between them.

DIGraph.py
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



