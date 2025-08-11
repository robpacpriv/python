# run py code: CTRL + R
# format document by pep8: SHIFT + ALT + F

nothing = None                      #nothing
sometext = 'Hello sir Robik ...'    #string
somenumber = 10                     #intiger

#build-in functions:
print(sometext)
print(somenumber)

print(type(sometext))
print(type(somenumber))

print(len(sometext))

#methods:

print(sometext.upper()) #all high level
print(sometext.lower()) #all low level
print(sometext.capitalize()) #only first letter is high level
print(sometext.title()) #all first letters of words are high level
print(sometext.swapcase()) #all are in oposite way

print(sometext.isupper()) #checking if string is uppercase
print(sometext.islower()) #checking if string is lowercase
print(sometext.istitle()) #checking if the first character of each word is uppercase, and the rest are lowercase

print(sometext.count("l")) #how many times we have "l" inside sometext type

print(sometext.find("r")) #on which position we have "r" inside sometext type
print(sometext.find("R",8)) #on which position we have "R" inside sometext type after 8th position
print(sometext.find("R",8,-4)) #on which position we have "R" inside sometext type after 8th position and 4th from backwards

print(sometext.replace("Robik", "Papik"))


somenumber = str(somenumber) #conversion to string
print(type(somenumber))
print(somenumber)

# Challange Course 7: Data with Baraa
age = 42
height = 1.92
name = 'Robik'
student = False
nothingspecial = ""

print(age)
print(type(age))
print(height)
print(type(height))
print(name)
print(type(name))
print(len(name))
print(student)
print(type(student))
print(nothingspecial)
print(type(nothingspecial))
print(len(nothingspecial))
