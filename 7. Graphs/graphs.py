"""
Filename: graphs.py
Desription: Creates and manages Graph
Author: Priyankar Shivhare
Date: April 17, 2025
"""

class Graph():
    """ Instantiate and Manages a Graph"""
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        """Prints the adjacency matrix"""
        print(self.adj_list)

    def add_vertex(self, vertex):
        """Adds a vortex in the graph"""
        if vertex not in self.adj_list: # Add only if vortex doesn't exist
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        """Adds an edge to the graph"""
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        """Remove an Edge from the Graph"""
        if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, v1):
        """Removes the vertex from the Graph"""
        if v1 in self.adj_list:
            while len(self.adj_list[v1]) != 0:
                self.remove_edge(v1, self.adj_list[v1][0])
            self.adj_list.pop(v1)
            return True
        return False
