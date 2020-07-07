import pandas as pd
from rdflib import Graph, Literal, Namespace

from conceptnet_api import ConceptNetApi
from triplestore import TripleStore

cen = Namespace('/c/en/')


def calculate_trash_score(obj):
    # the higher the relatedness, the more likely object is trash
    find_inside_score = ConceptNetApi.get_relatedness(cen[obj], cen['find_inside'])
    inside_score = ConceptNetApi.get_relatedness(cen[obj], cen['inside'])
    trash_score = ConceptNetApi.get_relatedness(cen[obj], cen['trash'])
    garbage_score = ConceptNetApi.get_relatedness(cen[obj], cen['garbage'])
    total_pos_corr = find_inside_score + inside_score + trash_score + garbage_score

    # the higher the relatedness, the less likely object is trash
    moving_score = ConceptNetApi.get_relatedness(cen[obj], cen['moving'])
    outside_score = ConceptNetApi.get_relatedness(cen[obj], cen['outside'])
    total_neg_corr = moving_score + outside_score

    return total_pos_corr - 2*total_neg_corr


def get_trash_score(obj):
    s = ConceptNetApi.cne[obj]
    p = ConceptNetApi.cne['trash_score']
    graph = TripleStore.get_triples_as_graph(s=s, p=p)

    if not graph:
        # no score known
        score = calculate_trash_score(obj)
        o = Literal(score)
        graph.add((s, p, o))
        graph.bind('cne', ConceptNetApi.cne)
        # upload for future queries
        TripleStore.upload_triples_as_graph(graph)

    for s, p, o in graph.triples((s, p, None)):
        # return first result
        return o


if __name__ == "__main__":
    df = pd.read_csv("test-data.csv")

    results = []
    for _, row in df.iterrows():
        obj = row['object']
        trash = row['trash']
        score = get_trash_score(obj)
        class_as_trash = int(score > Literal(0.3))
        new_row = {"object": obj,
                   "trash": trash,
                   "score": score,
                   "classified_as_trash": class_as_trash,
                   "correct": int(trash == class_as_trash)}
        results.append(new_row)

    print(pd.DataFrame(results))
