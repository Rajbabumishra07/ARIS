"""
ARIS Weather Module
Author : Raj Babu Mishra

P1.5
Weather Information Module
Uses Open-Meteo public API
No API key required
"""

import requests


# =========================================================
# WEATHER MODULE
# =========================================================

def get_weather(city="Prayagraj"):

    try:

        # -------------------------------------------------
        # Geocoding
        # -------------------------------------------------

        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        results = geo_data.get("results")

        if not results:

            return f"Sir, I couldn't find the location {city}."

        location = results[0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        location_name = location.get(
            "name",
            city
        )

        country = location.get(
            "country",
            ""
        )

        # -------------------------------------------------
        # Weather
        # -------------------------------------------------

        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "precipitation,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data.get(
            "current",
            {}
        )

        # -------------------------------------------------
        # Values
        # -------------------------------------------------

        temperature = current.get(
            "temperature_2m"
        )

        feels_like = current.get(
            "apparent_temperature"
        )

        humidity = current.get(
            "relative_humidity_2m"
        )

        precipitation = current.get(
            "precipitation"
        )

        wind_speed = current.get(
            "wind_speed_10m"
        )

        weather_code = current.get(
            "weather_code"
        )

        condition = weather_description(
            weather_code
        )

        # -------------------------------------------------
        # Response
        # -------------------------------------------------

        return (
            f"Weather in {location_name}, {country}\n"
            f"Condition : {condition}\n"
            f"Temperature : {temperature}°C\n"
            f"Feels Like : {feels_like}°C\n"
            f"Humidity : {humidity}%\n"
            f"Precipitation : {precipitation} mm\n"
            f"Wind Speed : {wind_speed} km/h"
        )

    except requests.exceptions.Timeout:

        return (
            "Sir, the weather service is taking too long "
            "to respond."
        )

    except requests.exceptions.RequestException:

        return (
            "Sir, I couldn't connect to the weather service."
        )

    except Exception as error:

        print(
            "Weather Error:",
            error
        )

        return (
            "Sir, I couldn't get the weather information."
        )


# =========================================================
# WEATHER CODE
# =========================================================

def weather_description(code):

    weather_codes = {

        0:
            "Clear sky",

        1:
            "Mainly clear",

        2:
            "Partly cloudy",

        3:
            "Overcast",

        45:
            "Fog",

        48:
            "Depositing rime fog",

        51:
            "Light drizzle",

        53:
            "Moderate drizzle",

        55:
            "Dense drizzle",

        61:
            "Slight rain",

        63:
            "Moderate rain",

        65:
            "Heavy rain",

        71:
            "Slight snow",

        73:
            "Moderate snow",

        75:
            "Heavy snow",

        80:
            "Slight rain showers",

        81:
            "Moderate rain showers",

        82:
            "Violent rain showers",

        95:
            "Thunderstorm",

        96:
            "Thunderstorm with slight hail",

        99:
            "Thunderstorm with heavy hail"
    }

    return weather_codes.get(
        code,
        "Unknown weather"
    )