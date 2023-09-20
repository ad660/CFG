import requests
from pprint import pprint as pp

appid = '545a5f53adb70d09fb133d7b181d07eb'
endpoint = 'https://api.openweathermap.org/data/2.5/weather'

# pokemon = input('Enter a pokemon ')
userInput = input('Put in ID pls ')
url = f'https://pokeapi.co/api/v2/pokemon/{userInput}'

queryparams = {
    'q': 'London, UK', 
    'appid': appid,
    'units': 'imperial'
    }


response = requests.get(url).json()
pp(response)
