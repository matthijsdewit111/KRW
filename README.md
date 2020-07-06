# KRW

## Getting started

Make sure you have a GraphDB repo named `asimov`.

Run `init_triplestore.py` to initialize local GraphDB triplestore with namespaces and such.

## Run experiments

Run `experiment_conceptnet.py` to get an evaluation of our method to classify items as trash or not using conceptnet

## Further information

`triplestore.py` contains interface to commincate with GraphDB api/repo
`conceptnet_api.py` contains interface to commicate with conceptnet api
`reset_triplestore.py` clears some data from GraphDB triplestore