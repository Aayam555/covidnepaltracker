from flask import Flask, jsonify
from flask_cors import CORS
from covid_info.covid_info_world import covid_info_world
from covid_info.covid_info_nepal import covid_info_nepal

app = Flask(__name__)
CORS(app)

@app.route("/api/covid_info_world")
def world():
	return jsonify(covid_info_world())

@app.route("/api/covid_info_nepal")
def nepal():
	return jsonify(covid_info_nepal())


app.run(host="0.0.0.0")