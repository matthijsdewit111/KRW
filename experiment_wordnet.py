import pandas as pd
from nltk.corpus import wordnet
from rdflib import Graph, Literal, Namespace

from triplestore import TripleStore


def calculate_trash_score(obj):
    if obj == "garbage_bag":
        obj = "bag"
    if obj == "plastic_bottle":
        obj = "bottle"
    if obj == "broken_glass":
        obj = "glass"
    obj_wn = wordnet.synset(obj + '.n.01')
    # the higher the relatedness, the more likely object is trash
    inside = wordnet.synset('inside.n.01')
    trash = wordnet.synset('trash.n.01')
    inside_score = obj_wn.wup_similarity(inside)
    trash_score = obj_wn.wup_similarity(trash)
    total_pos_corr = inside_score + trash_score

    # the higher the relatedness, the less likely object is trash
    outside = wordnet.synset('outside.n.01')
    outside_score = obj_wn.wup_similarity(outside)
    total_neg_corr = outside_score

    return total_pos_corr - 2*total_neg_corr


def get_trash_score(obj):
    wnns = Namespace('http://wordnet.princeton.edu/')
    s = wnns[obj]
    p = wnns['trash_score']
    graph = TripleStore.get_triples_as_graph(s=s, p=p)

    if not graph:
        # no score known
        score = calculate_trash_score(obj)
        o = Literal(score)
        graph.add((s, p, o))
        graph.bind('wn', wnns)
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
        class_as_trash = int(score > Literal(-0.1))
        new_row = {"object": obj,
                   "trash": trash,
                   "score": score,
                   "classified_as_trash": class_as_trash,
                   "correct": int(trash == class_as_trash)}
        results.append(new_row)

    print(pd.DataFrame(results))
