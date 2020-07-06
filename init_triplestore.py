from rdflib import Namespace
from triplestore import TripleStore
from conceptnet_api import ConceptNetApi

# add namespaces
r1 = TripleStore.add_namespace('cn', ConceptNetApi.cn)
r2 = TripleStore.add_namespace('cne', ConceptNetApi.cne)
if not r1 or not r2:
    print("couldn't add a namespace")
    print(r1, r2)