print(f"\nPython Organizing Data - MIMO App")
print(f"****************************************************\n")

print("-Lists")
cars = ["ford","mazda","fiat"] 
print(f"cars list: {cars}")

print(f"first car: {cars[0]}") #access first element of the list

cars[2] = "Tesla" #access and change value of the element with indice 2 
print(f"cars list updated: {cars}")

last_car = cars.pop() #pop deletes the last element of the list 
print(f"last car deleted: {last_car}")
print(cars)

cars.append("Subaru") #append adds to the end of the list
cars.insert(1, "Tesla") #insert can add a value by giving the index to be added at
print(cars)

mixed_list = ["Name", 8, 3.44, False] #Python allows mixed type values in a list 
print(f"\nMixed list: {mixed_list}\n")

user_scores = [12, 43, 53, 100, 11, 14]
print(f"Minimum score: {min(user_scores)}") #minimum value in the list
print(f"Maixmum score: {max(user_scores)}") #maximum value in the list
print(f"Sum of scores: {sum(user_scores)}") #sum the values in the list
user_scores.sort() #sort the list in ascending order
print(f"Sorted scores: {user_scores}")

vocabulary = ["Hi", "Bye", "Nice"]
print(f"\n{vocabulary}")
vocabulary.sort()
print(f"{vocabulary}")
print(f"****************************************************\n")

print("-String Manipulation")
full_name = "John Lee"
name = full_name.split() #default way to split is the whitespace
print(name)
name_update = full_name.replace("Lee", "Robert") #replace some part of the string 
print(name_update)

signups = "44-22-44-11"
signups_list = signups.split("-") #here we use - as the way we want it to split the string 
print(signups_list)
print(f"****************************************************\n")

print("-Casting")
#Python will convert the integer to a float automatically
bill = 21.4
tip = "3.5"
total = bill + float(tip) #float casting
print("The total is " + str(total)) #string casting 

bill = int(12.9) #int casting never rounds it just consider the integer 
print(bill)

user_1 = [1, "Sara"]
user_2 = [2, "Andy"]
data = dict([user_1, user_2]) #dict() can be used with a list of the lists 
print(data)
print(f"****************************************************\n")

humidity_level = [87, 74, 82, 48]
humidity_level.insert(0, 90)
humidity_level.pop()
print(f"Humidity list: {humidity_level}")
print(f"List length: {len(humidity_level)}") #length of the list, amount of values in the list

flavors = ["strawberry", "apple", "pineapple"]
print(f"\nFlavors: {flavors}")
ratings = [9, 5 ,8]
print(f"Ratings: {ratings}")
passed = [True, False, True]
print(f"Release: {passed}")
add_lists = flavors + ratings + passed
print(f"Full lists: {add_lists}")

#Store and display latest, highest, and lowest stock values
stock_values=[298.4, 301.4, 297.4, 300.5, 265.8]
highest_value = stock_values[0]
lowest_value = stock_values[0]

for value in stock_values:
    if value > highest_value:
        highest_value = value
    if value < lowest_value:
        lowest_value = value
latest_value = stock_values.pop()
print(f"\nList: {stock_values}")
print(f"Latest value: {latest_value}")
print(f"Highest value: {highest_value}")
print(f"Lowest value: {lowest_value}")

#Find dataset largest and smallest value and difference
sizes = [30, 34, 28, 29]
largest = max(sizes)
smallest = min(sizes)
difference = largest - smallest
print(f"\nList: {sizes}")
print(f"Largest value: {largest}")
print(f"Smallest value: {smallest}")
print(f"Difference: {difference}")

#Store two teams in a list, check if they have the same length, then display the rounds left based on the length
team_1 = ["Mia", "Lisa", "Liam"]
team_2 = ["Ava", "James", "Tyler"]

size_1 = len(team_1)
size_2 = len(team_2)

if size_1 != size_2:
    print(f"\nTeams must have the same size")
else:
    print(f"\nGame on")

while(size_1 > 0):
    print(f"Rounds left: {size_1}")
    size_1-=1

#Count how many one and five-star ratings there are in a list and display the results
ratings = [5, 3, 5, 3, 1, 4, 5, 5, 1, 3]
five_star = ratings.count(5)
one_star = ratings.count(1)
amounts = [five_star, one_star]
print(f"\nList of ratings: {ratings}")
print(f"Amount of five start {amounts[0]}")
print(f"Amount of one start {amounts[1]}")

#A club has a membership sign-up form where the data arrives as strings. Let's change types to fix it. 
name_box = "Alice Bentall"
age_box = "20"
uni_box = ""
subs_box = "1.99"
mkt_box = "0"
name_entered = bool(name_box)
if name_entered:
    name = name_box
else:
    name = "Unknown"
age = int(age_box)
student = bool(uni_box)
subscription = float(subs_box)
marketing = bool(int(mkt_box))
profile = name + ", "+ str(age) + ", subscription:" + str(subscription)
print(profile)
print(f"****************************************************\n")