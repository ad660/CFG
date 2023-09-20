import requests
# REST API - data source that can be accessed through libraries by using specific comands. 

# GET - Retrives data 

# POST - Adds new data to server

# PUT - Change existing info

# DELETE - Deletes existing information  

# ENDPOINTS = API url of a server 

################MakingAPI request################


url = "https://yummly2.p.rapidapi.com/feeds/list"

querystring = {"limit":"24","start":"0"}

headers = {
	"X-RapidAPI-Key": "fe96bdb19dmshe4b8c86e4fdcf01p13d7b4jsn3cfdcad9eda3",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())