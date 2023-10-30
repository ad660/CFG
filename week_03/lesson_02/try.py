# try:
#     den = int(input("Please enter a number to divide by"))
#     result = 100 / den
#     print(result)
# except ZeroDivisionError:
#     print("you cannot divide by 0, try again")
# except ValueError:
#     print("cannot convert to integer")

# Else and Finally are optional 

# class ValueIsBelowHundredError(ValueError):
#     pass 

# number = int(input("Please enter number above 100"))

# if number < 100:
#     raise ValueIsBelowHundredError("Value is below 100")


def debugging():
    my_list = []
    for i in range(10):
        new_i = 10 + i

        # import pdb
        # pdb.set_trace()

        print("new value is: ", i)
        my_list.append(new_i)
    
    return my_list