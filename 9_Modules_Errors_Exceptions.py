print(f"\nPython Modules, Errors and Exceptions - MIMO App")
print(f"****************************************************\n")

print(f"-Modules")
#We can add more organization to our code with a module
#Modules group related classes and data and make them accessible from one place
#Some modules are available online for people to use in their code

import math, statistics #built-in modules in Python

print("The value of pi is")
print(math.pi)

print(f"\nThe square root of 16 is")
print(math.sqrt(16))

print("\nRounded up to the nearest number")
rounded = math.ceil(22.7324)
print(rounded)

print("\nRounded down to the nearest number")
print(math.floor(44.32))

#help(math) #Find out more about the functionality of a module
#help(statistics)

scores = [4, 4, 3, 6, 5, 1, 2]
mean = statistics.mean(scores)
print(f"\nMean score is {mean}\n")

#If we want to extract only the functionality we care about
from math import pi #when we use from we don't need to add the name of the module anymore
print(pi)

#we can modify the name of the module we are importing
import statistics as stats
sales = [34, 56, 72, 12, 98]
median = stats.median(sales)
print(median)

print(f"****************************************************\n")
print(f"-Errors")
#SyntaxError are usually due to typos, such as misspelled keywords or putting a keyword in the wrong place, leaving out symbols such as colons and brackets, incomplete statements
#IndentationError can result from incorrect or missing indentation
#^, known as a caret, indicates in the console where the error has been found in the code
#ZeroDivisionError, cannot divide number by zero
print(f"****************************************************\n")
print(f"-Exceptions")
#Python will raise an exeption when it cannot perform an operation
#share = size/6 raises NameError: name 'size' is not defined, referencing a variable that doesn't exist
#The text shown in the console when an exception is raised is called the traceback. 
#KeyError, when you are trying to retrieve a key that is not in the dictionary
#TypeError, when the type of elements cannot work together
#AttributeError when objects may not have attributes or methods that we think they have
#Traceback is best read from bottom to top, to understand what went wrong with the code
#ModuleNotFoundError - Python cannot find a module
#IndexError - if an index is out of range

#A logic error occurs when there is no error or exception, but our code does not work correctly. 
print(f"****************************************************\n")
print(f"-Raising Exceptions")
#Sometimes we want to raise an exception when a condition we have defined is not met
#The raise keyword is used to raise an exception. We can define both the kind of error, and the error message, like here with ValueError
slices = 18
diners = 0
if diners < 1:
    raise Exception("There must be at least one diner")
else:
    slices_each = slices / diners

age = -3
if not age >= 0:
    raise ValueError('Age cannot be negative')

#We can use exceptions to highlight when something cannot be working as it should be 
predicted_sales = -5
if predicted_sales < 0:
    raise ValueError("predicted_sales cannot be negative")

#We can use conditions to validate inputs, and raise an exception when the conditions are not met. 
scores = [125, 60, 189, 88, 16]
if min(scores) < 0 or max(scores) > 180:
  raise ValueError('Error in scores')

age = 1000 
try: 
 adult_years = age - 18 
except: 
 raise TypeError("Input is not a number") 
else: 
 if adult_years > 150: 
  raise ValueError("Age is too large")
#A try and except block can be used for exception handling
try:
    login(user)
except:
    print('User not known, please try again')
#Try and Except tend to be used when we know there is a chance of the operation not being possible
#We can use pass if we want nothing to be executed after except:
try:
    print("Hello, " + user)
except:
    pass

#We can use an else statement at the end if we want to execute some code only when no error has been raised
details = {"name": "Helena",
           "occupation": "carpenter",
           "age": 35}

try: 
  age = details["age"]
except:
 raise NameError("No age value in record")
else:
 print(f"Maximum heart rate is {220 - age}")

#We can use a finally statement at the end if we want to execute some related code regardless of whether an error was raised
entry = 50
try:
 result = entry * 1.5
except:
 raise ValueError("result cannot be calculated")
else:
  print(result)
finally:
  print("Try another value?")
