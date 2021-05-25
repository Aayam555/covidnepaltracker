from flask import Flask, jsonify
from flask_cors import CORS
from covid_info.covid_info_world import covid_info_world
from covid_info.covid_info_nepal import covid_info_nepal
from flag_images.flag_images_data import flag_images_data

app = Flask(__name__)
CORS(app)

@app.route("/api/covid_info_world")
def world():
	return jsonify(covid_info_world())

@app.route("/api/covid_info_nepal")
def nepal():
	return jsonify(covid_info_nepal())

@app.route("/api/covid_info_flags")
def flags():
	return jsonify(flag_images_data)


app.run(debug=True)