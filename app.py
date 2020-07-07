from flask import Flask, render_template
import experiment_conceptnet
import experiment_conceptnet_size
import experiment_wordnet
from rdflib import Literal

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cntrash/<obj>")
def cntrash(obj):
    score = experiment_conceptnet.get_trash_score(obj)
    return str(score > Literal(0.3))

@app.route("/wntrash/<obj>")
def wntrash(obj):
    score = experiment_wordnet.get_trash_score(obj)
    return str(score > Literal(-0.1))

@app.route("/cnsize/<obj>")
def cnsize(obj):
    size_score = experiment_conceptnet_size.get_size_score(obj)
    class_as = "S"
    if size_score > Literal(0.1):
        class_as = "L"
    elif size_score > Literal(0.0):
        class_as = "M"
    return class_as
    
if __name__ == "__main__":
    app.run(debug=False)