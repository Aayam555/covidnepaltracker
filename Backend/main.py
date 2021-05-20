from flask import Flask, jsonify
from covid_cases.covid_cases import covid_cases

app = Flask(__name__)

@app.route("/api/covid_cases")
def cases():
	return jsonify(covid_cases())


app.run(debug=True)
	