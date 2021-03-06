import requests
from rdflib import Namespace

class ConceptNetApi:
    cn = Namespace("http://api.conceptnet.io/")
    cne = Namespace("http://api.conceptnet.io/c/en/")

    @staticmethod
    def get_related_concepts(concept):
        response = requests.get('{}related{}'.format(ConceptNetApi.cn, concept), params={"filter": "/c/en"})
        if not response.ok:
            print(response.content)
            return
        
        related_terms = response.json()['related']
        ids = []
        for item in related_terms:
            ids.append(ConceptNetApi.cn[item['@id'][1:]])
        return ids

    @staticmethod
    def get_relatedness(concept1, concept2):
        response = requests.get('{}relatedness'.format(ConceptNetApi.cn), params={"node1": concept1, "node2": concept2})
        if not response.ok:
            print(response.content)
            return
        
        relatedness = response.json()['value']
        return relatedness

if __name__ == "__main__":
    r = ConceptNetApi.get_relatedness('/c/en/trash', '/c/en/trash_bag')
    print(r)

    rc = ConceptNetApi.get_related_concepts('/c/en/trash')
    for c in rc:
        print(c)
