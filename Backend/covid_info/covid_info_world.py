from bs4 import BeautifulSoup
import requests

URL = "https://www.worldometers.info/coronavirus/#countries"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "lxml")


def table_countries_data():
	# Getting table countries
	covid_cases_table_countries = soup.select("#main_table_countries_today > tbody:nth-child(2)")

	# Extracting tr tag from covid_cases_table_countries
	covid_cases_table_countries_tr = covid_cases_table_countries[0].find_all("tr")

	# Data
	covid_cases_table_countries_data = []

	for table_row in covid_cases_table_countries_tr:
		country_info = table_row.text
		country_info = country_info.split("\n")


		for country in country_info:
			if country_info[0].isdigit():
				country_info.pop(0)

		country_info_processed_data = []

		for info in country_info:
			if "," in info:
				while "," in info:
					info = info.replace(",", "")

			if "+" in info:
				while "+" in info:
					info = info.replace("+", "")

			country_info_processed_data.append(info)

		try:
			data = {"country": country_info_processed_data[2],
					 "total_cases": country_info_processed_data[3].replace(" ", ""),
					 "new_cases": country_info_processed_data[4],
					 "total_deaths": country_info_processed_data[5],
					 "new_deaths": country_info_processed_data[6],
					 "total_recovered": country_info_processed_data[7],
					 "new_recovered": country_info_processed_data[8],
					 "active_cases": country_info_processed_data[9],
					 "serious_critical": country_info_processed_data[10],
					 # "population": country_info_processed_data[13],
					 # "continent": country_info_processed_data[14]
					}

		except Exception:
			pass

		covid_cases_table_countries_data.append(data)

	return covid_cases_table_countries_data

def covid_info_world():
	'''
	This function returns covid cases of world and countries
	'''
	return table_countries_data()
