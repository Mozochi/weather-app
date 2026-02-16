import get_weather


def displayData(menuOption: int, key: str, url: str):
    if menuOption != 9:
        userLocation = input("Enter location: ")

    match menuOption:
        case 1:
            displayCurrentWeather(get_weather.getCurrentWeather(key, url, userLocation))
        case 2:
            days = input("How many days to forecast?: ")
            displayForecast(get_weather.getForecast(key, url, userLocation, days))
        case 9:
            exit()
        case _:
            print("Option not found. Please enter an number from the options above.")

def displayCurrentWeather(data: dict):
    temps = data["temps"]
    wind = data["wind"]
    rain = data["rain"]
    location = data["location"]
    print(f"""Current Weather for {location[0]}, {location[1]}: 
          \n\nTemperature: {temps[0]}°C\nFeels Like: {temps[1]}°C\nWind Chill: {temps[2]}°C
          \n\nWind: {wind[0]}mph\nWind Gusts: {wind[1]}mph\nWind Direction: {wind[2]}
          \n\nPrecipitation: {rain[0]}mm\nHumidity: {rain[1]}%\nCloud Cover: {rain[2]}%""")
    
def displayForecast(data: dict):
    location = data[1]
    forecastData = data[0]
    print(f"""Weather forecast for {location[0]}, {location[1]}:\n""")
    for key, value in forecastData.items():
        print(f"Forecast for {key}:\n")
        
        for forecastKey, forecastValue in value.items():
            match forecastKey:
                case "maxtemp_c":
                    print(f"Daily Maximum Temperature: {forecastValue}°C")
                case "mintemp_c":
                    print(f"Daily Minimum Temperature: {forecastValue}°C")
                case "avgtemp_c":
                    print(f"Daily Average Temperature: {forecastValue}°C")
                case "totalprecip_mm":
                    print(f"Total Precipitation: {forecastValue}mm")
                case "daily_chance_of_snow":
                    print(f"Chance of snow: {forecastValue}%\n\n")
                case "maxwind_mph":
                    print(f"Maximum Wind Speed: {forecastValue}mph")
