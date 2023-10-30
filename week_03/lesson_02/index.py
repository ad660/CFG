def apply_discount(product, discount):
    price = round(product['price'] * (1 - discount /100), 2)
    assert 0 <= price <= product['price']
    return price 

# assert = value checking if its true 

# It is as produce [price] because its running through a dictionary

trainers = {'name': 'trainers', 'price': 79.99}

print(apply_discount(trainers, 200)) 

# If you do 200 you get an assertion error because the discount puts the price as less than 0 which makes the assertion false

####### HANDLING EXCEPTIONS ######

try:
    den = int(input("Please enter a number to divide by"))
    result = 100 / den
    print(result)
except ZeroDivisionError:
    print("you cannot divide by 0, try again")
except ValueError:
    print("cannot convert to integer")

# Else and Finally are optional 

######## MAKING OUR OWN EXCEPTIONS #########


class ValueIsBelowHundredError(ValueError):
    pass 

number = int(input("Please enter number above 100"))

if number < 100:
    raise ValueIsBelowHundredError("Value is below 100")