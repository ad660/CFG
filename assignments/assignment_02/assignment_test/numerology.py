import requests
from datetime import datetime

# I have used the date time module as my additional module. You can install this using pip install datetime. 

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def writeFile(dictionary, lifepathNum):
    currentTime = datetime.now().strftime("The date is %A %m %Y and the time is %H:%M:%S")
    f = open("NumerologyResult.txt", "w")
    f.write("Welcome to your numerology result! \n\n")
    f.write(f"Your life path number is {lifepathNum} \n\n")
    f.write(f'{dictionary} \n\n')
    f.write(currentTime)

# This is where you can find the API key to test it yourself: https://rapidapi.com/Alejandro99aru/api/horoscope-astrology/

url = "https://horoscope-astrology.p.rapidapi.com/numerology"


headers = {
	"X-RapidAPI-Key": "fe96bdb19dmshe4b8c86e4fdcf01p13d7b4jsn3cfdcad9eda3",
	"X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
}

# Created this function to take the numbers passed into it and change them into a list that we can add together 


def numerologyNumber(num):
    querystring = {"n":{num}}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    descriptionData = data['desc']
    return descriptionData


def addNumbers(fullnumber):
    finalNumber = 0

    result = [int(x) for a,x in enumerate(str(fullnumber)) ]
    for digit in result:
        finalNumber += digit
    return finalNumber

    # print(result)


def calcYear(birth_year):
    birth_year_list = list(birth_year)
    totalSum = 0


    for number in birth_year_list:
        totalSum += int(number)
    
    return addNumbers(totalSum)
           

        # return totalSum

# calcYear('1995') - This can be used to test the function
    


def calcMonth(monthofBirth):
    
     for month in months: 
         if monthofBirth == month:            
            numberOfMonth = months.index(month) + 1
            if (numberOfMonth < 10):
                return numberOfMonth
            if (numberOfMonth >= 10):
                stringNum = str(numberOfMonth)
                listStringNum = list(stringNum) 
                monthResult = int(listStringNum[0]) + int(listStringNum[1])
                # Okay so this works to add together the numbers but I want to make a function that you can pass in a number and have it 
                return monthResult 
     
            #  print('invalid input')
            #  print(month, monthofBirth)







def intro():
    print('Your birth date is made up of three parts -- the month, day, and year -- and your Life Path number is essentially a sum of these numbers.')
    print('Please enter your birthday starting with the Year, Month then Day as prompted')
    print('First step is to reduce the numbers in your day. month then year. If you were born before November (11th month) your number will will stay the same')


    # This will get the month of birth and convert it to its number by checking what index it matches to in the list above and cross referencing that to the index and adding 1. It adds 1 because the list starts at 0 and we want to make sure we get the number of the month.  

    dayOfBirth = int(input('Please enter the day of your birth e.g if you were both on the 12th please enter "12" '))
    dayNum = addNumbers(dayOfBirth)
    print(f'Your day number is {dayNum}')

    playerBirthMonth = input('Please enter what month you were born ').capitalize()
    monthNum = calcMonth(playerBirthMonth)
    print(f'Your month number is {monthNum}')

    playerBirthYear = input('Please enter year in this format e.g. "1997" ')
    yearNum = calcYear(playerBirthYear)
    print(f'Your year number is {yearNum}')


    lifePathNumberPreliminary = dayNum + monthNum + yearNum
    lifePathNumber = addNumbers(lifePathNumberPreliminary)

    print(f'Your life path number is {lifePathNumber}')
    print(numerologyNumber(lifePathNumber))
    stringOfResult = str(numerologyNumber(lifePathNumber))
    writeFile(stringOfResult, lifePathNumber)

intro()

