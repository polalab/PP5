# relations
with open("relations1.txt") as f:
    relation_txt = f.read()

relations_lines = relation_txt.split('\n')  # split on enter
relations_lines = relations_lines[1::]  # remove utff

relations = {}

for rela in relations_lines:
    relation_names = rela.split(' ')
    relations[relation_names[0]] = relation_names[1::]

print(relations)




