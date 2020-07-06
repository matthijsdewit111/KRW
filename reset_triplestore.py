import pandas as pd
from triplestore import TripleStore
from conceptnet_api import ConceptNetApi

df = pd.read_csv("test-data.csv")

for obj in df['object']:
    print(obj)
    TripleStore.remove_triples(s=ConceptNetApi.cne[obj])