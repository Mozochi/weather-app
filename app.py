import os
from dotenv import load_dotenv

from display_data import displayData

load_dotenv()
API_KEY = os.getenv("KEY")
BASE_URL = "http://api.weatherapi.com/v1"

def main():
    while True:
        try:
            userOption = int(input("Menu Options: \n1. Get current weather for a location\n2. Get weather forecast for a location\n9. Exit\n>"))
            displayData(userOption, API_KEY, BASE_URL)
            input("\nPress any key to continue...")
        except Exception as e: 
            print(f"Error: {e}\n")
        


if __name__ == "__main__":
    main()
    