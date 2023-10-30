def age_validation(age):
    if age < 0:
        raise ValueError("Only positive itegers are allowed")
    
    assert 12 < age <= 19

    return True

def name_validation(name):
    if ',' not in name:
        raise ValueError("incorrect input: missing ',' to separate names")

    firstname, surname = name.split(',')

    if not len(firstname) or not len(surname): 
        raise ValueError("Incorrect input: missing first name or surname value")
    
is_successful = False 

try: 
    name = input("Please input name and surname separated by comma")
    name_validation(name)
    age = int(input("Enter age: "))
    age_validation(age)
except ValueError:
    print("Invalid input")
except AssertionError:
    print("Age is not in the teenager category")
else: 
    with open("reg.txt", 'a+') as file:
        file.write(f"New member name: {name} new member age: {age}")
        is_successful = True
finally:
    if is_successful:
        print("Registration Successful")
    else: 
        print("Could not complete registration")
