# https://www.bogotobogo.com/python/python_graph_data_structures.php

class Node:
    def __init__(self, node):
        self.node = node
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
# TODO
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0