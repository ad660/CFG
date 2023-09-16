from importingModules.module import my_name

name = input('What is your name') #gets user input


print('Hello, {}'.format(name)) #This is an older verion of doing it. You can see 'format' 
print(f'Hello {name}') #This is a format string which is a more widely used version. 

print(my_name)