import requests

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

# Created this function to take the numbers passed into it and change them into a list that we can add together 

def numerologyNumber(num):
    querystring = {"n":{num}}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

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

# calcYear('1995')
    


# def simpleMonth(janToOctober):
#     monthResult =  


def calcMonth(monthofBirth):
    
     for month in months: 
         if monthofBirth == month:            
            numberOfMonth = months.index(month) + 1
            print(f"Month number is {numberOfMonth}")
            if (numberOfMonth >= 10):
                stringNum = str(numberOfMonth)
                listStringNum = list(stringNum) 
                monthResult = int(listStringNum[0]) + int(listStringNum[1])
                # print(f'Your month number is {monthResult}')
                print(f'This is the result if you are born after october{monthResult}')
                # Okay so this works to add together the numbers but I want to make a function that you can pass in a number and have it 
            if (numberOfMonth < 10):
                return monthResult if numberOfMonth >= 10 else numberOfMonth
            else:
                print('Invalid input')
     
            #  print('invalid input')
            #  print(month, monthofBirth)






url = "https://horoscope-astrology.p.rapidapi.com/numerology"


headers = {
	"X-RapidAPI-Key": "fe96bdb19dmshe4b8c86e4fdcf01p13d7b4jsn3cfdcad9eda3",
	"X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
}

def intro():
    print('Your birth date is made up of three parts -- the month, day, and year -- and your Life Path number is essentially a sum of these numbers.')
    print('Please enter your birthday starting with the Year, Month then Day as prompted')
    print('First step is to reduce the numbers in your month. If you were born before November (11th month) your number will will stay the same')
    
    playerBirthMonth = input('Please enter what month you were both ').capitalize()
    monthNum = calcMonth(playerBirthMonth)
    print(monthNum)

    playerBirthYear = input('Please enter year in this format e.g. "1997" ')
    yearNum = calcYear(playerBirthYear)
    print(yearNum)

    # This will get the month of birth and convert it to its number by checking what index it matches to in the list above and cross referencing that to the index and adding 1. It adds 1 because the list starts at 0 and we want to make sure we get the number of the month.  

    dayOfBirth = int(input('Please enter the day of your birth e.g if you were both on the 12th please enter "12" '))
    dayNum = addNumbers(dayOfBirth)
    print(dayNum)

    lifePathNumberPreliminary = dayNum + monthNum + yearNum
    lifePathNumber = addNumbers(lifePathNumberPreliminary)

    print(f'Your life path number is {lifePathNumber}')
    print(numerologyNumber(lifePathNumber))

intro()





# pickNumber()