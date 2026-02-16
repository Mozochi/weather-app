import requests

def getCurrentWeather(key: str, url: str, loc: str) -> dict: 
    """
    Docstring for getCurrentWeather
    
    :param key: API Key
    :type key: str
    :param url: API URL
    :type url: str
    :param loc: Geographical location to find weather (e.g. London)
    :type loc: str
    :return: {temps: [temp_c, feelslike_c, windchill_c], wind: [wind_mph, gust_mph, wind_dir], rain: [precip_mm, humidity, cloud], location" [location name, country]}
    :rtype: dict
    """
    response = requests.get(
        url=f"{url}/current.json",
        params={"key": key, "q":loc}
    )

    if response.status_code == 200:
        responseData = response.json()
        currentData = responseData["current"] # Getting only the current weather data

        weatherData = {"temps": [currentData["temp_c"], currentData["feelslike_c"], currentData["windchill_c"]],
                       "wind": [currentData["wind_mph"], currentData["gust_mph"], currentData["wind_dir"]],
                       "rain": [currentData["precip_mm"], currentData["humidity"], currentData["cloud"]],
                       "location": [responseData["location"]["name"], responseData["location"]["country"]]
                       }
        
        return weatherData 
    return {}


def getForecast(key: str, url: str, loc: str, days: int) -> dict:
    """
    Docstring for getForecast
    
    :param key: API Key
    :type key: str
    :param url: API URL
    :type url: str
    :param loc: Geographical location to find weather (e.g. London)
    :type loc: str
    :param days: Number of days to forecast
    :type days: int
    :return: Returns a dict of forecast data, and the location for the forecast as a list
    :rtype: dict, list
    """
    response = requests.get(
         url=f"{url}/forecast.json",
         params={"key": key, "q":loc, "days": days}
    )
    if response.status_code == 200:
        responseData = response.json()
        forecast = responseData["forecast"]
        forecastData = {}
        
        for day in forecast["forecastday"]:
            for key, value in day.items():
                if key == "day":
                    forecastData[f"{day['date']}"] = value
        return forecastData, [responseData["location"]["name"], responseData["location"]["country"]]
    
    return forecastData
