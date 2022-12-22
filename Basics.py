# Snake Case: Variable names with multiple words, use '_', such as home_city
# = assigns a value to a variable while == is an operator that compares two values  
print(f"\nPython Intro - MIMO App")
print(f"****************************************************\n")

print("-Update Variable")
status = "Watching Netflix" 
print(status)
status = "Styding Pyton" # = assigns a new value to the same variable
print(status)

print(f"\n-Store new value in another variable")
new_status = "Cooking a meal" # = assigns another value to a new variable
status = new_status # = assigns a variable to another variable 
print(new_status)
print(status)
print(f"****************************************************\n")

print("-True, False and the not operator")
correct = True
incorrect = not True #False
print(correct)
print(incorrect)
correct = False
incorrect = not False #True
print(correct)
print(incorrect)
available = True
out_of_stock = not available
print(not available) #False
print(out_of_stock)
print(f"****************************************************\n")

print("-Operators used for comparison")
print(10==10) #equality operator
print(10!=10) #inequality operator
print(10<=10) #less than or equal operator
print(10<10) #less operator
print(10>=10) #greater than or equal operator
print(10>10) #greater operator
print("apple"=="apple") 
print("subscribed"!="unsubscribed")
print(f"****************************************************\n")

print("-Variable Types")
sugar_content="High" #String
print(sugar_content)

score = 42 #Integer
print(score)

pi = 3.14159
print(pi) #Float

is_on = True #Boolean
print(is_on)
print(f"****************************************************\n")

print("-Formatted Strings")
#Allow us to display expressions like adding a string to a number, wihtout any error
print(f"{2} new messages")
messages_unread = 4
print(f"{messages_unread} new messages")
field = "nano"+"tech"
print(field + " trading")
tries = 4
current_try = 1
print(f"{tries - current_try} tries left")
print(f"****************************************************\n")

#Compare jeans_sold with target to see if the retailer hit their sales target. Then we will check if there are eans still in stock.
stock = 600
target = 500
jeans_sold = 400

target_hit = jeans_sold == target
print(f"Was target hit? {target_hit}")

current_stock = stock - jeans_sold
in_stock = current_stock != 0 
print(f"In stock? {in_stock}")

#Program that updates how many cars we have rented and how many are available for rent 
total = 100
rented_cars = 40
available = total - rented_cars
print(f"{available} available cars")
rented_cars += 3 
available = total - rented_cars
print(f"{available} available cars")

languages = "Python"
languages += " SQL"
print(languages)
print(f"****************************************************\n")