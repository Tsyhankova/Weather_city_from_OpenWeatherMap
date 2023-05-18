# Weather_city_from_OpenWeatherMap

<p class="has-line-data" data-line-start="1" data-line-end="2">Here is a simple implementation of a weather forecast application using the OpenWeatherMap API. Here’s a breakdown of what the code does:</p>
<ol>
<li class="has-line-data" data-line-start="2" data-line-end="3">The code starts by importing the necessary libraries: pprint for pretty printing, requests for making HTTP requests, and parse from dateutil.parser for parsing dates.</li>
<li class="has-line-data" data-line-start="3" data-line-end="6">The OpenWeatherForecast class is defined, which serves as a wrapper for accessing weather forecast data from the OpenWeatherMap API. It has an internal _city_cache dictionary to cache weather forecasts for different cities.<br>
•   The <strong>init</strong> method initializes the _city_cache dictionary.<br>
•   The get method retrieves the weather forecast for a given city by making an HTTP request to the OpenWeatherMap API using the city name. The forecast is returned in Celsius units.</li>
<li class="has-line-data" data-line-start="6" data-line-end="9">The CityInfo class is defined to represent information about a specific city and its weather forecast.<br>
•   The <strong>init</strong> method initializes the city attribute and an optional weather_forecast attribute. If no weather_forecast object is provided, it defaults to creating a new instance of OpenWeatherForecast.<br>
•   The weather_forecast method uses the weather_forecast object to retrieve the weather forecast for the city specified in the city attribute.</li>
<li class="has-line-data" data-line-start="9" data-line-end="14">The _main function is defined, which is the entry point of the program.<br>
•   It creates an instance of OpenWeatherForecast called weather_forecast.<br>
•   It iterates five times in a loop, creating a CityInfo instance for the city “Wroclaw” with the weather_forecast object.<br>
•   It retrieves the weather forecast for “Wroclaw” using the weather_forecast method of the city_info object.<br>
•   Finally, it prints the forecast using pprint.pprint.</li>
<li class="has-line-data" data-line-start="14" data-line-end="16">The <strong>name</strong> check ensures that the _main function is only executed if the script is run directly and not imported as a module.<br>
Overall, the code demonstrates how to fetch weather forecast data for a specific city using the OpenWeatherMap API and the OpenWeatherForecast and CityInfo classes.</li>
</ol>
