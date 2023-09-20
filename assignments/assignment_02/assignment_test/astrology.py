import requests 
import json

url = "https://astrologer.p.rapidapi.com/api/v3/birth-chart"

parameters = {

}

payload = {
	"name": "Test",
	"year": 2000,
	"month": 10,
	"day": 10,
	"hour": 10,
	"minute": 10,
	"longitude": 45,
	"latitude": 45,
	"city": "Roma",
	"timezone": "Europe/Rome",
	"language": "IT"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "fe96bdb19dmshe4b8c86e4fdcf01p13d7b4jsn3cfdcad9eda3",
	"X-RapidAPI-Host": "astrologer.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

astrology = response.json()

jprint(astrology[1])


# Main programme 

# def startGame():
#     playersName = input("Welcome to the horoscope maker \n lets start by giving us your name")

#     def saveToFile(playersName, filename):
#         with open(filename) as file:
#             file.write(f'This is {playersName}\'s horrorscope')

