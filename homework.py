#homework
from graph_class import Node
#EX.1 Implement ```print_neighbours ```  **_method_** in graph_class which prints all neighbours for given node vex
#E.g. in out example for Maciek it should print 'Pola'
#plan
#first define the method - what parameters do you need? in a class, probably self and what is the other?
#make it look at a given dictionary
#say that the keys are nodes
#iterate through the dictionary to add neighbours to nodes?
#give names to node's neighbours
#print neighbours

#Ex. 2
#Take a look at the ```relations2.txt``` notice that you have only six lines there. Notice that
#each of them represents an edge in the graph. Write a **function** in main.py that will build a relations
#dictionary based only on those edges. Make sure that the graph you represent is an undirected one!
#You can get inspired by the ```cheatsheet.py``` file
with open("relations2.txt") as f:
    relation_txt_2 = f.read()
def build_relations_dict(edges):
    relations = {}
    relations_lines = edges.split('\n')[0::]
    for edge in relations_lines:
        person1, person2 = edge.split()
        if person1 not in relations:
            relations[person1] = [person2]
        else:
            relations[person1].append(person2)
        if person2 not in relations:
            relations[person2] = [person1]
        else:
            relations[person2].append(person1)
    return relations
print(build_relations_dict(relation_txt_2))

#ex. 3
#What would you do if the edges were directed?
def build_directed_relations_dict(nodes):
    relations = {}
    relations_lines = nodes.split('\n')[0::]
    for edge in relations_lines:
        source, target = edge.split()
        if source not in relations:
            relations[source] = [target]
        else:
            relations[source].append(target)
    return relations
print(build_directed_relations_dict(relation_txt_2))

#ex. 4
#**Try** to, instead of making a relation dictionary, build a graph_class