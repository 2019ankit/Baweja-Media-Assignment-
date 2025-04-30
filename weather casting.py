"""
Write a Python script that does the following:
1. Use a public API (e.g., OpenWeatherMap, JSONPlaceholder, or any free API of your
choice).
2. Make an API request to fetch some data.
3. Process and print specific information from the response in a clean format.
(e.g., for a weather API – print current temperature and weather condition for a
given city).
"""


import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extracting specific information
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        city = data['name']
        country = data['sys']['country']

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition.capitalize()}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    # API Key Integration 
    api_key = "4f2af99f0d36480d26731a18a0e3e5d3"
    city_name = input("Enter a city name: ")
    get_weather(city_name, api_key)
