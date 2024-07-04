from flask import Flask, render_template, request
from rdflib import Graph

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    sparql_query = request.form['sparql_query']
    g = Graph()
    g.parse('life_expectancy_rdf_dataset.ttl', format='ttl')
    g.parse('relay_whs_rdf_dataset.ttl', format='ttl')
    qres = g.query(sparql_query)
    headers = [str(var) for var in qres.vars]
    results = [[str(term) for term in row] for row in qres]
    return render_template('index.html', headers=headers, results=results)

if __name__ == '__main__':
    app.run(debug=True)
