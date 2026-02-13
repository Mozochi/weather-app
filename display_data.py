from get_weather import getCurrentWeather


def displayData(menuOption: int, key: str, url: str):
    match menuOption:
        case 1:
            userLocation = input("Enter location: ")
            displayCurrentWeather(getCurrentWeather(key, url, userLocation), userLocation)
        case 9:
            exit()

def displayCurrentWeather(data: dict, location: str):
    temps = data["temps"]
    wind = data["wind"]
    rain = data["rain"]
    print(f"""Current Weather for {location}: 
          \n\nTemperature: {temps[0]}°C\nFeels Like: {temps[1]}°C\nWind Chill: {temps[2]}°C
          \n\nWind: {wind[0]}mph\nWind Gusts: {wind[1]}mph\nWind Direction: {wind[2]}
          \n\nPrecipitation: {rain[0]}mm\nHumidity: {rain[1]}%\nCloud Cover: {rain[2]}%""")