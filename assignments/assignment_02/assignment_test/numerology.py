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

def calcYear(birth_year):
    birth_year_list = list(birth_year)
    totalSum = 0
    addedSum = 0

    for number in birth_year_list:
        totalSum += int(number)
        while totalSum > 0:
            digit = totalSum % 10
            addedSum += digit
            addedSum // 10
        print(addedSum)
        # return totalSum

calcYear()
    




def calcMonth(monthofBirth):
    
     for month in months: 
         if monthofBirth == month:            
            numberOfMonth = months.index(month) + 1
            print(f"Month number is {numberOfMonth}")
            if (numberOfMonth >= 10):
                stringNum = str(numberOfMonth)
                listStringNum = list(stringNum) 
                monthResult = int(listStringNum[0]) + int(listStringNum[1])
                print(f'Your month number is {monthResult}')
                # Okay so this works to add together the numbers but I want to make a function that you can pass in a number and have it 
            break
     
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
    calcMonth(playerBirthMonth)

    playerBirthYear = input('Please enter year in this format e.g. "1997" ')
    calcYear(playerBirthYear)

    # This will get the month of birth and convert it to its number by checking what index it matches to in the list above and cross referencing that to the index and adding 1. It adds 1 because the list starts at 0 and we want to make sure we get the number of the month.  

    # monthofBirth = input('Please enter what month you were both').capitalize

    # for month in months: 
    #     if monthofBirth == month:            
    #         print(f'month of birth is {months.index(month)} ')
    #         numberOfMonth = months.index(month) + 1
    #         print(f"Month number is {numberOfMonth}")

    #         if (numberOfMonth > 10):
    #             numberOfMonth.split(1, 1)
    #         break
    #     else: 
    #         print('invalid input')
    #         print(month, monthofBirth)


    dayOfBirth = int(input('Please enter the day of your birth e.g if you were both on the 12th please enter "12" '))

# intro()


def pickNumber():
    userInput = int(input("Please pick a number "))
    querystring = {"n":{userInput}}
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())


# pickNumber()