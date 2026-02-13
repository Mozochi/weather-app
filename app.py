import os
from dotenv import load_dotenv

from displayData import displayData

load_dotenv()
API_KEY = os.getenv("KEY")
BASE_URL = "http://api.weatherapi.com/v1"

def main():
    while True:
        userOption = int(input("Menu Options: \n 1. Get current weather for a location\n 9. Exit\n>"))
        displayData(userOption, API_KEY, BASE_URL)

        input("\nPress any key to continue...")
        
                



if __name__ == "__main__":
    main()
    