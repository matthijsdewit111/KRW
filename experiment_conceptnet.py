import pandas as pd
from rdflib import Graph, Literal

from conceptnet_api import ConceptNetApi
from triplestore import TripleStore

def calculate_trash_score(obj):
    return 0.5

def get_trash_score(obj):
    s = ConceptNetApi.cne[obj]
    p = ConceptNetApi.cne['trash_score']
    graph = TripleStore.get_triples_as_graph(s=s, p=p)

    if not graph:
        # no score known
        score = calculate_trash_score(obj)
        o = Literal(score)
        graph.add((s, p, o))
        # upload for future queries
        TripleStore.upload_triples_as_graph(graph)

    for s, p, o in graph.triples((s, p, None)):
        # return first result
        return o


if __name__ == "__main__":
    df = pd.read_csv("test-data.csv")

    for obj in df['object']:
        print(obj)
        score = get_trash_score(obj)
        print(score)
