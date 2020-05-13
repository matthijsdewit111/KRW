import requests
from rdflib import Graph, ConjunctiveGraph, Literal, BNode, Namespace, RDF, URIRef

entity_examples = ["car", "person", "bike", "house", "motorcycle", "scooter", "street_lamp", "garbage_bag", "furniture",
                   "christmas_tree", "mattress", "trash_bin", "container"]

g = Graph()


def add_triple(triple):
    subject = URIRef("http://api.conceptnet.io{}".format(triple[0]))
    predicate = URIRef("http://api.conceptnet.io{}".format(triple[1]))
    object = URIRef("http://api.conceptnet.io{}".format(triple[2]))
    g.add((subject, predicate, object))


# get all (limited in this case to 100) relations of an entity
for entity in entity_examples:
    print(entity)
    obj = requests.get('http://api.conceptnet.io/c/en/{}?limit=100'.format(entity)).json()
    for edge in obj['edges']:
        triple = (edge["start"]["@id"], edge["rel"]["@id"], edge["end"]["@id"])
        print("########start of statement########")
        print(triple)
        print("########end of statement########")
        add_triple(triple)
raw_ttl = g.serialize(format='turtle').decode("utf-8")
print(raw_ttl)
with open("example2.ttl", "w") as fp:
    fp.write(raw_ttl)
# find how much two entities are related (in this case determine how likely the entity is to be found inside or outside)
# for entity in entity_examples:
#     print(entity)
#     obj = requests.get(
#         'http://api.conceptnet.io/relatedness?node1=/c/en/{}&node2=/c/en/find_inside'.format(entity)).json()
#     print("inside:", obj['value'])
#     obj = requests.get(
#         'http://api.conceptnet.io/relatedness?node1=/c/en/{}&node2=/c/en/find_outside'.format(entity)).json()
#     print("outside:", obj['value'])
