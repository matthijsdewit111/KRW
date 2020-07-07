import pandas as pd
from rdflib import Graph, Literal, Namespace

from conceptnet_api import ConceptNetApi
from triplestore import TripleStore

cen = Namespace('/c/en/')


def calculate_size_score(obj):
    # the higher the relatedness, the more likely object is trash
    small_score = ConceptNetApi.get_relatedness(cen[obj], cen['small'])
    light_score = ConceptNetApi.get_relatedness(cen[obj], cen['light'])
    total_pos_corr = small_score + light_score

    # the higher the relatedness, the less likely object is trash
    large_score = ConceptNetApi.get_relatedness(cen[obj], cen['large'])
    heavy_score = ConceptNetApi.get_relatedness(cen[obj], cen['heavy'])
    total_neg_corr = large_score + heavy_score

    return total_pos_corr - total_neg_corr


def get_size_score(obj):
    s = ConceptNetApi.cne[obj]
    p = ConceptNetApi.cne['size']
    graph = TripleStore.get_triples_as_graph(s=s, p=p)

    if not graph:
        # no score known
        score = calculate_size_score(obj)
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
        size = row['size']
        size_score = get_size_score(obj)
        print(obj, size_score)
        class_as = 0
        if size_score > Literal(0.0):
            class_as += 1
        if size_score > Literal(0.1):
            class_as += 1
        new_row = {"object": obj,
                   "size": size,
                   "score": size_score,
                   "classified_as": class_as,
                   "correct": int(size == class_as)}
        results.append(new_row)

    print(pd.DataFrame(results))
