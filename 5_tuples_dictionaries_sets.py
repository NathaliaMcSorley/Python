print(f"\nPython Tuples, Dictionaries, and Sets - MIMO App")
print(f"****************************************************\n")

print("-Tuples")
#We can group related pieces of data with a tuple. Tuples help us group different pieces of data that belong together. 
movies = ["Vertigo", "Parasite", 1958, 2019]
movie_tuples = [("Vertigo", 1958), ("Parasite", 2019)] #list that store two tuples, each touple is one value
vertigo_data = ("Vertigo", 1958) #a variable that stores a tuple
print(movie_tuples)
print(movie_tuples[0]) #accessing a tuple
print(len(movie_tuples)) #display length of tuples
print(vertigo_data)
print(vertigo_data[1]) #accessing second data in the tuple

for movie in movie_tuples:
    print(f"Movies: {movie}")

#The main difference of lists and tuples is that unlike lists, we can't update, add, or delete values from tuples. Tuples are immutable.
#We use tuples to store information that shouldn't be modified, like a person's name and birth date
#Tuples are useful because they allow us to return multiple values from a function. 
def get_scores_data(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return highest_score, lowest_score
scores = [31, 45,89,56]
data = get_scores_data(scores)
print(f"{data}\n")
highest = data[0]
smallest = data[1]
print(f"Smallest score: {smallest}")
print(f"Highest score: {highest}\n")
#Since tuples are immutable, we return a tuple whn we won't need to modify it, but just use the values 

#When we want to be able to modify the returned collection of values, then we return a list
def form_team(players):
    team = []
    team.append(players[0])
    team.append(players[2])
    return team
players = ["Sue", "Ed", "Ann", "Ty"]
team = form_team(players)
team [0] = "Chloe"
print(f"{team}\n")

def analyze_profit(gains, expenses):
  profit = gains - expenses
  after_taxes = 0.85 * profit
  above_mean = profit > 1000
  return profit, after_taxes, above_mean
print(analyze_profit(600,540))
print(f"****************************************************\n")

print("-Dictionaries")
#To associate a meaning to each value in a collection of values, we use a data structure called a dictionary 
locations = {"headquarters": "New York", "flagship": "Paris"} #headquarters and flagship are uniques keys within the dictionary
print(f"{locations}\n") #each key is associated with exactly one value

car_data = {
 "brand": "Cadillac",
 "year": 1960,
 "restoration": ["1990", "2018"],
 "rented": False
}
print(car_data)
print(car_data["brand"]) #access the values by their key

for car in car_data:
    print(car_data[car])

car_data["rented"] = True #Update a key value
print(car_data)

car_data["milage"] = 195 #Add a new key pair value
print(car_data)

print("year" in car_data) #check if a dictionary contains a certain key

has_owner = "owner" in car_data
print(has_owner)

milage = car_data.pop("milage") #removing a key
print(car_data)
print(f"{milage}\n")

#It's a good practice to first use the in keyword to check if the key exists, before removing and avoiding getting an error
ticket = { 
    "seat no.": 25,
    "window": True
}
if "destination" in ticket:
    ticket.pop("destination")
print(ticket)

#The key pair value can be a string, tuple, boolean or number
members_count = { 
    ("Sai", "Chloe", "Yumi"): 3
}
print(f"\n{members_count}\n")
print(f"****************************************************\n")

print("-Sets")
#when we want to make sure that a collection of values can't have any duplicates, we store it in a set, like these postcodes here. 
postcodes = {"SW1A", "SY3", "B44"}
print(postcodes)
postcodes.add("SA89") #add element to the set
print(postcodes)
postcodes.add("SA89") #nothing happens when we use add() with an already existing value
print(postcodes)
postcodes.remove("SA89") #Delete element 
print(f"{postcodes}\n")

#to avoid getting an error, first check if an element is in a set before removing it
classes = {"Geometry", "Music", "French"}
if "History" in classes:
    classes.remove("History")
print(f"{classes}\n")

#sets are unordered, meaning that set elements don't have indices
#we can only check if a set contains an element like "no" with the in keyword
answer_options = {"yes", "no"}
print("no" in answer_options)
#we can also use a for loop to iterate through set elements and access them one by one
for answer in answer_options:
    print(f"Option: {answer}")
print(f"****************************************************\n")

print("-Sets and Lists")
#Lists allow duplicates, to eliminate duplicates from a list, we can transform it into a set 
grocery_list = ["broccoli", "cereal", "milk", "broccoli"]
print(set(grocery_list))
grocery_set = set(grocery_list)

print(f"****************************************************\n")

print("-Set Operations")
friends = {"Emma", "Jen", "Rob", "Ed"}
chat = {"Jen", "Ed", "Sue"} #subset of the friends set
print(f"Length of friends set: {len(friends)}") #length of the set
print(f"Is chat a subset of friends? {chat.issubset(friends)}") #check if chat is a subset of friends
#union gives us a new set without duplicates
#create a set of elements that are present in both sets
#elements that are in classmates but are NOT in friends
union = friends.union(chat)
intersection = friends.intersection(chat)
difference = friends.difference(chat)
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")