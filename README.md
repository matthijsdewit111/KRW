# KRW

## Getting started

Make sure you have a GraphDB repo named `asimov`.

(Optional) Run `init_triplestore.py` to initialize local GraphDB triplestore with namespaces.

Run `app.py` to start a local webserver at http://127.0.0.1:5000/

## Run experiments

Run `experiment_*.py` to get an evaluation of our method across some test data (`test-data.csv`)

Or query objects using the webpage, input an object name, like car, plastic_bottle or anything else, and press query.

## Further information

`triplestore.py` contains interface to commincate with GraphDB api/repo  
`conceptnet_api.py` contains interface to commicate with conceptnet api  
`reset_triplestore.py` clears some data from GraphDB triplestore to reset experiments