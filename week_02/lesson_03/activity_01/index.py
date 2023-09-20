# yourPassword = 'password123'

# def attemptPassword(password):
#     if (password == yourPassword):
#         print('Password correct: user logged in')
#     else:
#         print('password incorrect: try again')
#     return

# userAttempt = input('Please enter password')
# attemptPassword(userAttempt)


# def orderFood(price): 
    
#     if (price > 20):
#         print('This is out of budget')
#         discount_applicable = input('would you like a discount?')
#         if (discount_applicable == 'y'):
#             newPrice = price * 0.80
#             print(f'You total price is now {newPrice} as you have recieved a 20% discount')
#             if (newPrice > 20):
#                 print('This is still out of budget')
#             else:
#                 print(f'it costs {newPrice}, enjoy your food!')
#         else:
#             print(f'You have chosen not to apply a discount, your final price is {price}')
#     else:
#         print(f'Your final cost is {price} discount is not applicable on this order')


# enterPrice = int(input('Please enter a price '))
# orderFood(enterPrice)

# import random

# heads = 2 and 0
# tails = 1

# def flipCoin(userInput):
#     coinToss = random.randint(1, userInput) 
#     if (coinToss % heads):
#         print('You landed on heads')
#     elif (coinToss % tails):
#         print('You landed on tails')



# userInput = int(input('How many times will you flip the coin? '))
# flipCoin()


# PALINDROME 

def checkString(userInput): 
    check = userInput[::-1]
    print(check)
    return

checkString('Radio')
