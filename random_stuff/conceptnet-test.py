import requests

entity_examples = ["car", "person", "bike", "house", "motorcycle", "scooter", "street_lamp", "garbage_bag", "furniture", "christmas_tree", "mattress", "trash_bin", "container"]

# get all (limited in this case to 100) relations of an entity
# for entity in entity_examples:
#     print(entity)
#     obj = requests.get('http://api.conceptnet.io/c/en/{}?limit=100'.format(entity)).json()
#     for edge in obj['edges']:
#         print(edge['@id'])

# find how much two entities are related (in this case determine how likely the entity is to be found inside or outside)
for entity in entity_examples:
    print(entity)
    obj = requests.get('http://api.conceptnet.io/relatedness?node1=/c/en/{}&node2=/c/en/find_inside'.format(entity)).json()
    print("inside:", obj['value'])
    obj = requests.get('http://api.conceptnet.io/relatedness?node1=/c/en/{}&node2=/c/en/inside'.format(entity)).json()
    print("inside2:", obj['value'])
    obj = requests.get('http://api.conceptnet.io/relatedness?node1=/c/en/{}&node2=/c/en/garbage'.format(entity)).json()
    print("garbage:", obj['value'])
    obj = requests.get('http://api.conceptnet.io/relatedness?node1=/c/en/{}&node2=/c/en/trash'.format(entity)).json()
    print("trash:", obj['value'])

obj = requests.get('http://api.conceptnet.io/query?rel=/r/Synonym&node=/c/en/{}&other=/c/en'.format("garbage_bin")).json()
print(obj)
for edge in obj['edges']:
    print(edge['@id'])