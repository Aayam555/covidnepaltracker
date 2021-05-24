const get_data = async () => {
	let response = await fetch("https://covidnepaltracker.aayam555.repl.co/api/covid_info_nepal");
	let json = await response.json();

	return json;
}




const show_data = async () => {
	// Getting data from backend api endpoint
	covid_info_nepal = await get_data();

	// Breaking data into total_cases, total_recovered and total_deaths
	total_cases = covid_info_nepal.cases;
	total_recovered = covid_info_nepal.recovered;
	total_deaths = covid_info_nepal.deaths;
	image = covid_info_nepal.image;

	// Getting html elements
	display_total_cases = document.getElementById("total-cases");
	display_total_recovered = document.getElementById("total-recovered");
	display_total_deaths = document.getElementById("total-deaths");
	display_country = document.getElementById("display-country");

	// Displaying data
	display_total_cases.innerHTML = total_cases;
	display_total_recovered.innerHTML = total_recovered;
	display_total_deaths.innerHTML = total_deaths;
	display_country.innerHTML = `<img src="${image}"/><span class="country-name">Nepal<span>`;
}

show_data()