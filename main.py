"""graph representation"""
with open("relations1.txt") as f:
    relation_txt = f.read()
print(relation_txt)
print(type(relation_txt))

relations_lines = relation_txt.split('\n')[1::] #/n -> enter
print(relations_lines)
# find the graph here: https://app.diagrams.net/#G18j6pk-QIl-fFIeGPcsLGiuUphmgDlYaC

relations = {}
for element in relations_lines:
    relationships = element.split(' ')
    print(relationships)
    relations[relationships[0]] = relationships[1::]

print(relations)


