# KRW

## Getting started

Make sure you have a GraphDB repo named `asimov`.

(Optional) Run `init_triplestore.py` to initialize local GraphDB triplestore with namespaces.

Run `app.py` to start a local webserver at http://127.0.0.1:5000/

## Run experiments

Run `experiment_*.py` to get an evaluation of our method across some test data (`test-data.csv`).  
Running the `conceptnet` experiments gives some errors the first time you run it, since there is a restriction on how many times we can query from conceptnet. The solution is to wait 1 minute and try again, intermidiate results are stored in GraphDB triplestore so we don't need to query the onces we already queried the first time.

Or query objects using the webpage (run `app.py`), input an object name, like car, plastic_bottle or anything else, and press query.

## Further information

`triplestore.py` contains interface to commincate with GraphDB api/repo  
`conceptnet_api.py` contains interface to commicate with conceptnet api  
`reset_triplestore.py` clears some data from GraphDB triplestore to reset experiments