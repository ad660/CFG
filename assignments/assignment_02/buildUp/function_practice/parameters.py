def my_function(x, y, name):
    sum = f'{name} is {x} years old and has been living here for {y} years'
    return sum

print(my_function(30, 10, 'Angela'))

# Create a character using function parametres 

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
chosenfName = input('Please enter first name ')
chosenlName = input('Please enter last name ')
x = Person(chosenfName, chosenlName)
x.printname()


# Create a programme that asks for the first name and last name then asks you to choose between two different classes 

# class basePerson: 
#    def theSelf(self, fname, lname):
      