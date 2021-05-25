import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/country/nepal/"

def covid_info_nepal():
	'''
	This function returns total number of cases, deaths and recovered in Nepal
	'''

	response = requests.get(URL)
	soup = BeautifulSoup(response.text, "lxml")

	cases, deaths, recovered = soup.select("#maincounter-wrap > div > span")

	cases = cases.text
	deaths = deaths.text
	recovered = recovered.text

	image = f'''https://www.worldometers.info{soup.select(".content-inner")[0].find("img")["src"]}'''

	while "," in cases or "," in deaths or "," in recovered:
		try:
			cases = cases.replace(",", "")
			deaths = deaths.replace(",", "")
			recovered = recovered.replace(",", "")

		except:
			pass
	
	covid_info_nepal = {"cases": cases, "recovered": recovered, "deaths": deaths, "image": image}

	return covid_info_nepal