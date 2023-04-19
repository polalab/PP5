# https://www.bogotobogo.com/python/python_graph_data_structures.php

relations = {'Maciek': ['Pola'], 'Pola': ['Katrina', 'Maria', 'Vicky'], 'Katrina': ['Vicky', 'Archion', 'Pola', 'Maciek'], 'Archion': ['Katrina'], 'Maria': ['Pola'], 'Vicky': ['Pola', 'Katrina']}
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def print_neighbours(self, node):
        self.relations = {}
        if node not in self.relations:
            print("none")
        else:
            for neighbor in self.relations[node]:
                print(neighbor)

relations = {'Maciek': ['Pola'], 'Pola': ['Katrina', 'Maria', 'Vicky'], 'Katrina': ['Vicky', 'Archion', 'Pola', 'Maciek'], 'Archion': ['Katrina'], 'Maria': ['Pola'], 'Vicky': ['Pola', 'Katrina']}

maciek = Node('Maciek')
pola = Node('Pola')
katrina = Node('Katrina')
archion = Node ('Archion')
maria = Node('Maria')
vicky = Node('Vicky')

nodes = [maciek, pola, katrina, archion, maria, vicky]

for node in nodes:
    for neighbour in relations[node.name]:
        node.add_neighbour(Node(neighbour))

#print(maciek.neighbours)
#for nei in maciek.neighbours:
    #print(nei.name)


#print(maciek.name, maciek.neighbours)

exercise_1 = Node(relations)
print(exercise_1.print_neighbours("Pola"))