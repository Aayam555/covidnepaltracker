from bs4 import BeautifulSoup
import requests

URL = "https://www.worldometers.info/coronavirus/#countries"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")


def flag_images():
    '''
	This function is going to return the url for flags of all the countries

	This function is going to be used for only one time 
	because the data of flag images will hardly change in worldometer 
	if it changes we need to change the data as well by running this function

	This function will write a python file with dictionary of data with url of flag
	of different countries in worldometer. File is going to be saved in the same
	folder as this file and it will be saved as image_data.py
	'''

    list_of_url_of_countries = soup.select(".mt_a")
    processed_list_of_url_of_countries = [
        url["href"] for url in list_of_url_of_countries
    ]

    list_of_image_url = list()
    for processed_url in processed_list_of_url_of_countries:
        country_page_url = f"https://www.worldometers.info/coronavirus/{processed_url}"
        source_of_country_page = requests.get(country_page_url)
        soup_of_country_page = BeautifulSoup(source_of_country_page.text,
                                             "lxml")

        content_inner_class = soup_of_country_page.select(".content-inner")
        country_name = content_inner_class[0].find("h1").text
        image_url = content_inner_class[0].find("img")["src"]

        data = {"country_name": country_name.replace("\n \xa0", ""), "image_url": image_url}

        list_of_image_url.append(data)

        open("flag_images_data.py", "w").write(f"flag_images_data = {list_of_image_url}")


flag_images()
