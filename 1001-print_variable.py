# run py code: CTRL + R
# format document by pep8: SHIFT + ALT + F

print("\n----------------------------------\n")

# variable string type
name = ("\"Robik\"")
year = 43
year = str(year)

print("Hello", name)
print("Are you", year, "years old?")
print("It looks that", name, "is going learn Python ;-)")
print("That's great idea!")

print("\n----------------------------------\n")

# concate two string into variable string
fullprint = ("Hi again ") + name + ("Are you ") + year + (" years old?")

# show variable
print(fullprint)

print("\n----------------------------------\n")

# Using tripple hash
print("You Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI")

print("""\nYou Learning Path:
\t- Python Basics
\t- Data Engineering
\t- AI""")

print("\n----------------------------------\n")
# Challange Course 5: Data with Baraa

domain = ("pacula.eu")

print("datawithrobik@", domain, sep="")
print("support@", domain, sep="")
print("www.", domain, sep="")
