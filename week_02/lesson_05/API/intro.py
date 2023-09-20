# Application Programming Interface 

# Error codes
# 200 - OK
# 404 - Not found 
# 400 - Bad reqest 
# 500+ - Server issue 

import requests
from datetime import datetime
from pprint import pprint as mp

endpoint = 'http://api.open-notify.org/iss-now.json'

# Get request = getting info 
# Post requires me to send into 


response = requests.get(endpoint).json()

timestamp = response['timestamp']
location = response['iss_position']['latitude']


convertedTime = datetime.fromtimestamp(timestamp)

final = f'time in the spacestation is {convertedTime} and its location is {location}'

print(final)

# for person in response['people']:
#     print(person['name'])

