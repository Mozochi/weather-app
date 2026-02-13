import requests
import json

def getCurrentWeather(key: str, url: str, loc: str) -> dict: 
    """
    Docstring for getCurrentWeather
    
    :param key: API Key
    :type key: str
    :param url: API URL
    :type url: str
    :param loc: Geographical location to find weather (e.g. London)
    :type loc: str
    :return: {temps: [temp_c, feelslike_c, windchill_c], wind: [wind_mph, gust_mph, wind_dir], rain: [precip_mm, humidity, cloud]}
    :rtype: dict
    """
    response = requests.get(
        url=f"{url}/current.json",
        params={"key": key, "q":loc}
    )


    if response.status_code == 200:
        responseData = response.json()
        currentData = responseData["current"]

        weatherData = {"temps": [currentData["temp_c"], currentData["feelslike_c"], currentData["windchill_c"]],
                       "wind": [currentData["wind_mph"], currentData["gust_mph"], currentData["wind_dir"]],
                       "rain": [currentData["precip_mm"], currentData["humidity"], [currentData["cloud"]]]
                       }

        
        return weatherData 
    return {}



