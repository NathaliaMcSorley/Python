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
print(f"-Errors and Exceptions")
