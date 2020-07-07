import pandas as pd
from triplestore import TripleStore
from conceptnet_api import ConceptNetApi
from rdflib import Namespace

df = pd.read_csv("test-data.csv")
wnns = Namespace('http://wordnet.princeton.edu/')

for obj in df['object']:
    print(obj)
    TripleStore.remove_triples(s=ConceptNetApi.cne[obj])
    TripleStore.remove_triples(s=wnns[obj])
