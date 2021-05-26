const display = (total_cases, total_recovered, total_deaths, image, country) => {
	// Getting html elements
	let display_total_cases = document.getElementById("total-cases");
	let display_total_recovered = document.getElementById("total-recovered");
	let display_total_deaths = document.getElementById("total-deaths");
	let display_country = document.getElementById("display-country");

	// Displaying data
	display_total_cases.innerHTML = total_cases;
	display_total_recovered.innerHTML = total_recovered;
	display_total_deaths.innerHTML = total_deaths;
	display_country.innerHTML = `<img src="${image}"/><span class="country-name">${country}<span>`;
}


const covid_info_nepal_data = async () => {
	let covid_info_nepal_data_response = await fetch("https://covidnepaltracker.aayam555.repl.co/api/covid_info_nepal");
	let covid_info_nepal_data_json = await covid_info_nepal_data_response.json();

	return covid_info_nepal_data_json;
}




const show_covid_info_nepal = async () => {
	// Getting data from backend api endpoint
	let covid_info_nepal = await covid_info_nepal_data();

	// Breaking data into total_cases, total_recovered and total_deaths
	display(covid_info_nepal.cases, covid_info_nepal.recovered, covid_info_nepal.deaths, covid_info_nepal.image, "Nepal")
}

show_covid_info_nepal()


const covid_info_world_data = async () => {
	let covid_info_world_data_response = await fetch("https://covidnepaltracker.aayam555.repl.co/api/covid_info_world")
	let covid_info_world_data_json = await covid_info_world_data_response.json();

	window.localStorage.setItem("covid_info_world", JSON.stringify(covid_info_world_data_json));
}

const covid_info_flags_data = async () => {
	let covid_info_flags_response = await fetch("https://covidnepaltracker.aayam555.repl.co/api/covid_info_flags");
	let covid_info_flags_json = await covid_info_flags_response.json();

	window.localStorage.setItem("covid_info_flags", JSON.stringify(covid_info_flags_json));
}

covid_info_world_data()
covid_info_flags_data()

const filter_by_country = () => {
	let country_input = document.getElementById("country-input");
	let country_input_value = country_input.value;
	let covid_info_world = JSON.parse(window.localStorage.getItem("covid_info_world"));
	let covid_info_flags = JSON.parse(window.localStorage.getItem("covid_info_flags"));
	let country_flag_image_url = "";

	for (let image_index = 0; image_index < covid_info_flags.length; image_index++){
		if (country_input_value == "usa"){
			country_flag_image_url = "https://www.worldometers.info/img/flags/small/tn_us-flag.gif";
		}

		else if (country_input_value == "uk"){
			country_flag_image_url = "https://www.worldometers.info/img/flags/small/tn_uk-flag.gif";
		}

		else{
			if (covid_info_flags[image_index].country_name.toLowerCase().replace(" ", "") == country_input_value.toLowerCase()){
				country_flag_image_url = covid_info_flags[image_index].image_url;
			}
		}
		
	}

	for (let country_index = 0; country_index < covid_info_world.length; country_index++) {
		if (covid_info_world[country_index].country.toLowerCase() == country_input_value.toLowerCase()){
			covid_info_world_data_of_index = covid_info_world[country_index]
			display(covid_info_world_data_of_index.total_cases, covid_info_world_data_of_index.total_recovered, covid_info_world_data_of_index.total_deaths, country_flag_image_url, covid_info_world_data_of_index.country)
		}
	}


}

let country_input = document.getElementById("country-input");
country_input.addEventListener("keydown", (event) => {
	if (event.code == "Enter"){
		filter_by_country();
}})