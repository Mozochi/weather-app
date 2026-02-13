from get_weather import getCurrentWeather


def displayData(menuOption: int, key: str, url: str):
    match menuOption:
        case 1:
            userLocation = input("Enter location: ")
            displayCurrentWeather(getCurrentWeather(key, url, userLocation))
        case 9:
            exit()

def displayCurrentWeather(data: dict):
    temps = data["temps"]
    wind = data["wind"]
    rain = data["rain"]
    print(f"Current Weather: \nTemperature: {temps[0]}")