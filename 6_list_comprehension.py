print(f"\nPython List Comprehension - MIMO App")
print(f"****************************************************\n")
#A list comprehension is a way to create a new list by applying an expression on each element of an existing list
print("-List Comprehension")
#To create a list like halved based on another like prices, we need to first create an empty list, then fill it inside a loop
prices = [10, 46, 38, 48]
halved = []
for price in prices:
    half_price = price/2
    halved.append(half_price)
print(f"Using for loop: {halved}")

#We can build the same halved list as before, but in one line, using list comprehensions
halved_list = [price/2 for price in prices]
print(f"List Comprehension: {halved_list}\n")
#List comprehensions use for loops to iterate through each element of the original list

flights = ["1122", "5788", "0044"]
codes_a = ["BA" + flight for flight in flights]
print(f"List Comprehension: {codes_a}")

codes_b = []
for flight in flights:
  code = "BA" + flight
  codes_b.append(code)
print(f"Using for loop: {codes_b}")

codes = [flight for flight in flights]
print (f"Copy of flights list without changes: \n{codes}")
#List comprehensions work with elements of any type, like numbers, booleans, tuples or strings 

names = ["Smith", "Miller", "Brown"]
prefixed = ["Mr. " + name for name in names]
print(f"\nList Comprehension: {prefixed}")

words = ["apple", "aligator", "abracadabra", "avatar"]
a_count = [word.count("a") for word in words]
print(f"List Comprehension: {a_count}")
print(f"****************************************************\n")

print("-Functions as expression")
#We can only use functions that have a return statement since we are actually appending the returned value to the new list 
amount = [80, 38, 78, 96, 38]
def halve(num):
    return num/2
halved = [halve(price) for price in prices]
print(f"Using functions to create a list comprehension: {halved}")

authors = ["Virginia Wolf", "John Steinbeck"]

def add_comma(name):
  parts = name.split(" ")
  return parts[1] + ", " + parts[0]
authors_update = [add_comma(name) for name in authors]
print(authors_update)

scores = [156, 70, 100]
def passed(score):
  with_bonus = score + 10
  passed = with_bonus > 90
  return passed
passing_scores = [passed(score) for score in scores]
print(passing_scores)
print(f"****************************************************\n")

print("-Filtering with If Statements")
#We can use list comprehensions to create a new list by filtering elements of an existing one
scores = [12, 48, 37, 18, 29, 49, 58]
high_scores = [score for score in scores if score > 20]

websites = ["nytimes.com", "lemonde.fr", "economist.com"]
french = [website for website in websites if website.count(".fr") > 0]
print(french)
print(f"****************************************************\n")

print("-Negative Indexing and Deletion")
#Python allows us to use negative indexing to retrieve values from the end of an indexable object, such as a list
#Negative indexing means that we retrieve an element from the rightmost side of a list
users = ["Toby", "Tina", "Tom"]
last = users[-1]
print(last)
#We can use any negative value up to and including the length of the list, which would retrieve the first value
users = ["Jack", "Ahmed", "Elaine"]
users[-3] = "Jill"
print(users)
del users[-3]
print(users)

#We can use del with a key inside a dictionary to remove unwanted key: value pairs from the dictionary
product = {'category': 'book', 'price': 4.99, 'in_shop':True}
del product['in_shop']
print (product)

print(f"****************************************************\n")

print("-Slice Notation")
#Sometimes we want to retrieve multiple values from a list. We can do this using slicing. 
ingredients = ["eggs", "flour", "sugar", "salt"]
print(ingredients[0:2])
print(ingredients[2:]) #retrieve all values begging at position 2
#the value to the left of the colon is the start position for the slice. Python indexing starts at zero default.
#the value to the right of the colon is the stop position for the slice. Note that the element in the stop position is not included.
print(users[0:])
print(users[:])
print(users[-2:]) #Negative values mean 'start this many elements back from the end'.

#We can also use a format with two colons, [start: stop: step] where step determines how python steps between start and end
alphabet = ["A", "B", "C", "D", "E", "F"]
print(alphabet[1:6:2])
#2 means that we will return every second value 
#we can use step value with no star or end value
print(alphabet[::2])
print(f"****************************************************\n")

print("Hobbies prioritizer")
hobbies = ["Archery", "Bowling", "Canoeing", "Dance", "Embrooidery", "Flute", "Gymnastics"]
while hobbies[-1] != "Dance":
  del hobbies[-1]

number = str(len(hobbies))
print("These are your " + number + " favorite hobbies: ")
print(hobbies)