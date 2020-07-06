import requests
from rdflib import Graph
from io import StringIO


class TripleStore:
    url = "http://localhost:7200/repositories/asimov/"

    def __init__():
        # used as a static class, no instantiation needed
        pass

    @staticmethod
    def upload_triples_as_graph(graph):
        ttl = graph.serialize(format='turtle').decode("utf-8")
        TripleStore.upload_turtle(ttl)

    @staticmethod
    def upload_turtle(ttl):
        response = requests.post(TripleStore.url + "statements", data=ttl, headers={"Content-Type": "application/x-turtle"})
        return response.status_code == 204

    @staticmethod
    def add_namespace(prefix, value):
        response = requests.put(TripleStore.url + "namespaces/" + str(prefix), data=str(value))
        return response.status_code == 204

    @staticmethod
    def spo_to_params_dict(s, p, o):
        return dict((k, "<{}>".format(v)) for k, v in zip(["subj", "pred", "obj"], [s, p, o]) if v is not None)

    @staticmethod
    def get_triples(s=None, p=None, o=None):
        params = TripleStore.spo_to_params_dict(s, p, o)
        response = requests.get(TripleStore.url + "statements", headers={"Accept": "text/turtle"}, params=params)

        if response.status_code != 200:
            print(response.content)
            return None

        triples = response.content.decode('utf-8')
        return triples

    @staticmethod
    def get_triples_as_graph(s=None, p=None, o=None):
        triples = TripleStore.get_triples(s, p, o)
        g = Graph()
        g.parse(StringIO(triples), format="turtle")
        return g

    @staticmethod
    def remove_triples(s=None, p=None, o=None):
        params = TripleStore.spo_to_params_dict(s, p, o)
        response = requests.delete(TripleStore.url + "statements", headers={"Accept": "text/turtle"}, params=params)

        if response.status_code != 204:
            print(response.content)


if __name__ == "__main__":
    g = TripleStore.get_triples_as_graph(s="http://api.conceptnet.io/c/en/broken_glass")

    for s, p, o in g:
        print(s, p, o)
